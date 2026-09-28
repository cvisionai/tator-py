"""Dependency-scoped ACL migration helpers for migrate.py (no persisted state)."""
import argparse
import copy
import logging
from collections import defaultdict
from types import SimpleNamespace

logger = logging.getLogger(__name__)
TARGETS = ('project', 'media', 'file', 'section', 'algorithm', 'version',
           'target_organization', 'target_group', 'job_cluster', 'bucket',
           'hosted_template', 'localization', 'state')
GRANTEES = ('user', 'organization', 'group')
KINDS = {'target_organization': 'organization', 'target_group': 'group'}
# These fields are returned by the schema but not accepted by the RP REST endpoint.
UNSUPPORTED = {'localization', 'state'}


def mapping_pair(value):
    try:
        source, destination = map(int, value.split(':'))
        if source <= 0 or destination <= 0:
            raise ValueError()
        return source, destination
    except ValueError:
        raise argparse.ArgumentTypeError('Expected positive SOURCE_ID:DEST_ID')


def add_acl_arguments(parser):
    parser.add_argument('--skip_acl', action='store_true',
                        help='Disable ACL migration (enabled by default). ACL migration copies dependencies '
                             'and row protections for migrated resources. '
                             'Requires source and destination ACL administration access. '
                             'Mappings remain in memory; existing objects are rediscovered on reruns.')
    skip_help = {
        'organizations': 'Do not create organizations; still reuse matches/overrides.',
        'groups': 'Do not create groups or add group members; still reuse matches/overrides.',
        'affiliations': 'Do not copy organization affiliations.',
        'row_protections': 'Copy selected ACL dependencies without copying row protections.',
        'user_row_protections': 'Omit direct user-grantee RPs; group/organization grants remain eligible.',
    }
    for kind, help_text in skip_help.items():
        parser.add_argument('--skip_' + kind, action='store_true', help=help_text)
    for kind in ('organization', 'group'):
        parser.add_argument('--map_' + kind, type=mapping_pair, action='append', default=[],
                            metavar='SOURCE_ID:DEST_ID',
                            help='Override name matching for a selected ' + kind + ' (repeatable).')
    parser.add_argument('--acl_conflicts', choices=('error', 'source', 'destination'), default='error',
                        help='Different RP mask for the same targets/grantee: error (default) '
                             'source updates to the source mask; destination preserves the destination mask. '
                             'Missing RPs are still created. Unrelated destination rules are retained.')


def unique_named(objects, name, kind):
    matches = [obj for obj in objects if obj.name == name]
    if len(matches) > 1:
        raise ValueError(f'Ambiguous {kind} name {name!r}; use an explicit mapping')
    return matches[0] if matches else None


def rp_spec(row):
    return {key: getattr(row, key) for key in TARGETS + GRANTEES
            if getattr(row, key, None) is not None}


def rp_key(spec):
    return tuple(spec.get(key) for key in TARGETS + GRANTEES)


class ACLMigration:
    def __init__(self, args, source, destination, mappings=None, planning=False):
        self.args, self.source, self.destination = args, source, destination
        self.planning = planning
        self.counts = defaultdict(lambda: defaultdict(int))
        self._counted = set()
        self._next_planned_id = 0
        self.planned_media = {}
        self.maps = defaultdict(dict)
        self.maps.update(mappings or {})
        self.overrides = {}
        for kind in ('organization', 'group'):
            values = {}
            for old, new in getattr(args, 'map_' + kind):
                if old in values and values[old] != new:
                    raise ValueError(f'Conflicting {kind} mapping for {old}')
                values[old] = new
            self.overrides[kind] = values
        self.missing_users = set()
        self.acl_users = set()
        self.conflict_details = {}
        self.skipped = []
        self.organizations = {}
        self.groups = {}

    def planned_id(self):
        """Negative IDs represent not-yet-created objects and never reach the API."""
        self._next_planned_id -= 1
        return self._next_planned_id

    def count(self, kind, action, identity):
        key = (kind, action, identity)
        if key not in self._counted:
            self._counted.add(key)
            self.counts[kind][action] += 1

    def preview(self, dest_project, mappings, pending):
        """Run the same ACL traversal without any destination writes or live map changes."""
        plan = ACLMigration(copy.copy(self.args), self.source, self.destination,
                            {kind: dict(ids) for kind, ids in self.maps.items()}, planning=True)
        plan.owner = self.owner
        plan.maps.update({kind: dict(ids) for kind, ids in mappings.items()})
        plan.maps['project'][self.args.project] = dest_project.id if dest_project else plan.planned_id()
        for kind, objects in pending.items():
            for obj in objects:
                plan.maps[kind][obj.id] = plan.planned_id()
                if kind == 'media':
                    plan.planned_media[obj.id] = obj
        if plan.organization(plan.owner) is None:
            raise ValueError('Cannot resolve destination organization for project')
        plan.preserve_master_sections(dest_project.id if dest_project else None)
        plan.run()
        logger.debug('ACL preview counts describe explicit copies; server-generated defaults are reconciled during execution.')
        for kind in ('organizations', 'groups', 'group memberships', 'affiliations',
                     'row protections', 'ACL dependency sections'):
            counts = plan.counts[kind]
            if kind == 'affiliations' and self.args.skip_affiliations:
                logger.info('Skipping affiliations due to --skip_affiliations.')
                continue
            if kind == 'ACL dependency sections' and not any(counts.values()):
                continue
            details = [f"{counts['existing']} already exist"]
            for action, label in (('update', 'to update'), ('retained', 'destination masks retained'),
                                  ('skipped', 'skipped'), ('conflicts', 'conflicts')):
                if counts[action]:
                    details.append(f'{counts[action]} {label}')
            logger.info('%d %s will be created (%s).', counts['create'], kind, ', '.join(details))
        matched_users = plan.acl_users.intersection(plan.maps['user'])
        logger.info('ACL users: %d matched, %d skipped (no matching destination username).',
                    len(matched_users), len(plan.missing_users))
        if plan.counts['row protections']['conflicts']:
            for message in plan.conflict_details.values():
                logger.error('%s', message)
            raise ValueError('Resolve ACL conflicts before migration (see details above).')
        return plan.counts

    def skip(self, message):
        self.skipped.append(message)
        logger.debug('ACL migration: %s', message)

    def bind_project_organization(self, dest_project):
        """Validate the owner mapping before confirmation; this method never writes."""
        source_org = self.source.get_project(self.args.project).organization
        explicit = self.overrides['organization'].get(source_org)
        selected = dest_project.organization if dest_project else self.args.dest_organization
        if dest_project and self.args.dest_organization not in (None, selected):
            raise ValueError('--dest_organization disagrees with --dest_project')
        if explicit is not None and selected is not None and explicit != selected:
            raise ValueError('--map_organization disagrees with the destination project organization')
        selected = selected if selected is not None else explicit
        if selected is not None:
            self.destination.get_organization(selected)
            self.maps['organization'][source_org] = selected
        self.owner = source_org

    def prepare_project_organization(self):
        self.args.dest_organization = self.organization(self.owner)
        if self.args.dest_organization is None:
            raise ValueError('Cannot resolve destination organization for project')

    def user(self, old):
        if old is None:
            self.skip('Missing source user ID; dependent grant/membership skipped')
            return None
        self.acl_users.add(old)
        if old in self.maps['user']:
            return self.maps['user'][old]
        if old in self.missing_users:
            return None
        user = self.source.get_user(old)
        matches = self.destination.get_user_list(username=user.username)
        matches = [u for u in matches if u.username == user.username]
        if len(matches) > 1:
            raise ValueError(f'Ambiguous destination username {user.username!r}')
        if not matches:
            self.missing_users.add(old)
            self.skip(f'No destination user for {user.username!r}; dependent grants/members are skipped')
            return None
        self.maps['user'][old] = matches[0].id
        return matches[0].id

    def organization(self, old):
        if old not in self.organizations:
            self.organizations[old] = self.source.get_organization(old)
        if old in self.maps['organization']:
            if ('organizations', 'create', old) not in self._counted:
                self.count('organizations', 'existing', old)
            return self.maps['organization'][old]
        if old in self.overrides['organization']:
            new = self.overrides['organization'][old]
            self.destination.get_organization(new)
        else:
            org = self.organizations[old]
            match = unique_named(self.destination.get_organization_list(), org.name, 'organization')
            if match:
                new = match.id
            elif self.args.skip_organizations:
                self.count('organizations', 'skipped', old)
                self.skip(f'Organization {old} has no match and creation is skipped')
                return None
            else:
                # Do not copy storage configuration or automatic legacy membership grants.
                self.count('organizations', 'create', old)
                new = (self.planned_id() if self.planning else
                       self.destination.create_organization(organization_spec={
                           'name': org.name, 'permission_model': 'zerotrust',
                           'default_membership_permission': 'No Access'}).id)
        if new > 0 and ('organizations', 'create', old) not in self._counted:
            self.count('organizations', 'existing', old)
        self.maps['organization'][old] = new
        return new

    def group(self, old):
        if old in self.maps['group']:
            return self.maps['group'][old]
        group = self.source.get_group(old)
        self.groups[old] = group
        organization = self.organization(group.organization)
        if organization is None:
            self.count('groups', 'skipped', old)
            return None
        if old in self.overrides['group']:
            match = self.destination.get_group(self.overrides['group'][old])
            if match.organization != organization:
                raise ValueError(f'Group override {old} belongs to a different destination organization')
        else:
            match = (unique_named(self.destination.get_group_list(organization), group.name, 'group')
                     if organization > 0 else None)
        if match:
            new = match.id
            self.count('groups', 'existing', old)
        elif self.args.skip_groups:
            self.count('groups', 'skipped', old)
            self.skip(f'Group {old} has no match and creation is skipped')
            return None
        else:
            self.count('groups', 'create', old)
            new = (self.planned_id() if self.planning else
                   self.destination.create_group(organization, group_spec={'name': group.name}).id)
        self.maps['group'][old] = new
        if not self.args.skip_groups:
            members = {self.user(user) for user in (group.members or []) if user is not None}
            members.discard(None)
            existing = set(self.destination.get_group(new).members or []) if new > 0 else set()
            missing = sorted(members - existing)
            for user in members:
                self.count('group memberships', 'existing' if user in existing else 'create', (new, user))
            for user in (group.members or []):
                if user in self.missing_users:
                    self.count('group memberships', 'skipped', (old, user))
            if missing and not self.planning:
                self.destination.update_group(new, group_update_spec={'add_members': missing})
        else:
            for user in (group.members or []):
                self.count('group memberships', 'skipped', (old, user))
        return new

    def affiliations(self, old):
        if self.args.skip_affiliations:
            return
        new = self.maps['organization'][old]
        existing = ({a.user_id: a for a in self.destination.get_affiliation_list(new)
                     if a.user_id is not None}
                    if new > 0 else {})
        for affiliation in self.source.get_affiliation_list(old):
            user = self.user(getattr(affiliation, 'user_id', None))
            if user is None:
                self.count('affiliations', 'skipped', affiliation.id)
                continue
            if user not in existing:
                self.count('affiliations', 'create', (new, user))
                response = (SimpleNamespace(id=self.planned_id()) if self.planning else
                            self.destination.create_affiliation(new, affiliation_spec={
                                'user': user, 'permission': affiliation.permission}))
                self.maps['affiliation'][affiliation.id] = response.id
                existing[user] = SimpleNamespace(id=response.id, permission=affiliation.permission)
            else:
                self.count('affiliations', 'existing', (new, user))
                self.maps['affiliation'][affiliation.id] = existing[user].id
                if existing[user].permission != affiliation.permission:
                    self.count('affiliations', 'conflicts', (new, user))
                    self.skip(f"Affiliation permission differs for organization {old}, user {getattr(affiliation, 'user_id', None)}")

    def preserve_master_sections(self, dest_project):
        """Preserve the ACL origin, including master sections outside section selection."""
        if not self.maps['section'] and not self.maps['media']:
            return
        source_sections = {s.id: s for s in self.source.get_section_list(self.args.project)}
        dest_sections = ({s.id: s for s in self.destination.get_section_list(dest_project)}
                         if dest_project is not None else {})
        media = {old: (self.planned_media[old] if old in self.planned_media else self.source.get_media(old))
                 for old in self.maps['media']}
        pending = set(self.maps['section'])
        pending.update(m.master_section for m in media.values()
                       if getattr(m, 'master_section', None) is not None)
        visited = set()
        while pending:
            old = pending.pop()
            if old in visited:
                continue
            visited.add(old)
            section = source_sections[old]
            if old not in self.maps['section']:
                matches = [s for s in dest_sections.values() if s.name == section.name]
                if len(matches) > 1:
                    matches = [s for s in matches if s.path == section.path]
                if len(matches) > 1:
                    raise ValueError(f'Ambiguous master section {section.name!r}')
                if matches:
                    new = matches[0].id
                elif self.args.skip_sections:
                    raise ValueError(f'Master section {old} is unmapped and --skip_sections is set')
                elif self.planning:
                    self.count('ACL dependency sections', 'create', old)
                    new = self.planned_id()
                else:
                    import tator
                    new = tator.util.clone_section(self.source, old, dest_project, self.destination).id
                    dest_sections[new] = self.destination.get_section(new)
                self.maps['section'][old] = new
            master = getattr(section, 'master_section', None)
            if master is not None:
                pending.add(master)
        if self.planning:
            return
        for old, new in self.maps['section'].items():
            master = getattr(source_sections[old], 'master_section', None)
            if master is not None:
                mapped_master = self.maps['section'][master]
                if getattr(dest_sections[new], 'master_section', None) != mapped_master:
                    self.destination.update_section(new, section_update={'master_section': mapped_master})
        for old, obj in media.items():
            master = getattr(obj, 'master_section', None)
            if master is not None:
                new = self.maps['media'][old]
                mapped_master = self.maps['section'][master]
                if self.destination.get_media(new).master_section != mapped_master:
                    self.destination.update_media(new, media_update={'master_section': mapped_master})

    def run(self):
        """Follow target -> grantee dependencies, never grantee -> unrelated data."""
        logger.debug('Discovering ACLs visible to the source token; complete copying requires ACL access on every selected target.')
        # RP lists have scalar, exact-field filters, not project-descendant or bulk filters.
        # Index one visible snapshot rather than making one request per migrated media row.
        source_index = defaultdict(list)
        for row in self.source.get_row_protection_list():
            for field in TARGETS:
                old = getattr(row, field, None)
                if old is not None:
                    source_index[(field, old)].append(row)
        visited, rows = set(), {}
        while True:
            pending = [(field, old) for field in TARGETS
                       for old in self.maps[KINDS.get(field, field)]
                       if (field, old) not in visited]
            if not pending:
                break
            for field, old in pending:
                visited.add((field, old))
                for row in source_index[(field, old)]:
                    spec = rp_spec(row)
                    targets = [key for key in TARGETS if key in spec]
                    if not targets or any(key in UNSUPPORTED for key in targets):
                        self.count('row protections', 'skipped', row.id)
                        self.skip(f'RP {row.id} has unsupported targets')
                        continue
                    if any(spec[key] not in self.maps[KINDS.get(key, key)] for key in targets):
                        # In particular, never weaken a section+version rule by dropping one target.
                        self.count('row protections', 'skipped', row.id)
                        self.skip(f'RP {row.id} targets resources outside the migration mapping')
                        continue
                    grantees = [key for key in GRANTEES if key in spec]
                    if len(grantees) != 1:
                        raise ValueError(f'RP {row.id} must have exactly one grantee')
                    grantee = grantees[0]
                    if grantee == 'user' and self.args.skip_user_row_protections:
                        self.count('row protections', 'skipped', row.id)
                        continue
                    new = getattr(self, grantee)(spec[grantee])
                    if new is None:
                        self.count('row protections', 'skipped', row.id)
                        self.skip(f'RP {row.id} has an unresolved {grantee} grantee')
                        continue
                    rows[row.id] = row
        # Affiliations provide organization visibility and define organization-grantee audiences.
        for old in sorted(self.maps['organization']):
            self.affiliations(old)
        if not self.args.skip_row_protections:
            self.copy_rows(rows.values())
        else:
            for row in rows.values():
                self.count('row protections', 'skipped', row.id)
        logger.debug('ACL %s mapping totals: %s; %d incomplete dependencies/conflicts',
                    'preview' if self.planning else 'completed',
                    {kind: len(ids) for kind, ids in self.maps.items() if ids}, len(self.skipped))
        if not self.planning:
            logger.info('ACL migration complete (%d row protections mapped, %d skipped).',
                        len(self.maps['row_protection']), self.counts['row protections']['skipped'])
        return self.maps

    def describe_rule(self, spec):
        parts = []
        for field, value in spec.items():
            if value < 0:
                kind = KINDS.get(field, field)
                sources = [old for old, new in self.maps[kind].items() if new == value]
                parts.append(f'{field}=new (source IDs {sources})')
            else:
                parts.append(f'{field}={value}')
        return ', '.join(parts)

    def conflict(self, key, message):
        self.count('row protections', 'conflicts', key)
        self.conflict_details[key] = message
        if not self.planning:
            raise ValueError(message)

    def copy_rows(self, rows):
        existing = defaultdict(list)
        # Re-read after creating dependencies: these operations can generate default RPs.
        destination_targets = {field: set(self.maps[KINDS.get(field, field)].values())
                               for field in TARGETS}
        for row in self.destination.get_row_protection_list():
            spec = rp_spec(row)
            if any(spec.get(field) in destination_targets[field]
                   for field in TARGETS if field in spec):
                existing[rp_key(spec)].append(row)
        planned, actions = {}, []
        for row in rows:
            spec = {key: self.maps[KINDS.get(key, key)][value]
                    for key, value in rp_spec(row).items()}
            key = rp_key(spec)
            mask = int(row.permission)
            if (key in planned and planned[key][1] != mask and
                    not (self.args.acl_conflicts == 'destination' and existing[key])):
                previous_id, previous_mask = planned[key]
                self.conflict(key,
                    f'ACL conflict: source RPs {previous_id} (mask={previous_mask:#x}) and '
                    f'{row.id} (mask={mask:#x}) map to the same destination rule '
                    f'[{self.describe_rule(spec)}]. Resolve the source rules or mapping; '
                    '--acl_conflicts source cannot choose between conflicting source rules; '
                    'destination also requires an existing destination rule.')
                continue
            planned[key] = (row.id, mask)
            matches = existing[key]
            differing = [match for match in matches if int(match.permission) != mask]
            if differing and self.args.acl_conflicts == 'error':
                destination_rules = ', '.join(f'{match.id} (mask={int(match.permission):#x})'
                                              for match in differing)
                self.conflict(key,
                    f'ACL conflict: source RP {row.id} [{self.describe_rule(rp_spec(row))}] '
                    f'(mask={mask:#x}) maps to destination [{self.describe_rule(spec)}], '
                    f'which already has RP(s) {destination_rules}. '
                    'Use --acl_conflicts source to replace those destination masks, '
                    'or --acl_conflicts destination to retain them.')
                continue
            spec['permission'] = mask
            actions.append((row.id, key, spec))
        if self.planning:
            for old, key, spec in actions:
                if key in self.conflict_details:
                    continue
                matches = existing[key]
                if not matches:
                    self.count('row protections', 'create', key)
                elif any(int(match.permission) != spec['permission'] for match in matches):
                    if self.args.acl_conflicts == 'destination':
                        self.count('row protections', 'existing', key)
                        self.count('row protections', 'retained', key)
                    else:
                        self.count('row protections', 'update', key)
                else:
                    self.count('row protections', 'existing', key)
            return
        # Conflict detection finishes before the first RP mutation.
        for old, key, spec in actions:
            matches = existing[key]
            if matches:
                for match in matches:
                    if (int(match.permission) != spec['permission'] and
                            self.args.acl_conflicts != 'destination'):
                        self.destination.update_row_protection(match.id, row_protection_update_spec={
                            'permission': spec['permission']})
                        match.permission = spec['permission']
                new = matches[0].id
            else:
                response = self.destination.create_row_protection(row_protection_spec=spec)
                new = response.id
                # Only id and permission are needed when subsequent source rows share this key.
                existing[key].append(SimpleNamespace(id=new, permission=spec['permission']))
            self.maps['row_protection'][old] = new
