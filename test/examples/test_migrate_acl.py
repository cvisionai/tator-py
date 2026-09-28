"""Offline migration tests: python -m unittest discover -s test/examples -p test_migrate_acl.py."""
import argparse
import importlib.util
from pathlib import Path
import sys
from types import SimpleNamespace as Obj, ModuleType
import unittest
from unittest.mock import Mock, patch

EXAMPLES = Path(__file__).resolve().parents[2] / 'examples'
sys.path.insert(0, str(EXAMPLES))
from migrate_acl import ACLMigration, add_acl_arguments, rp_spec

# The migration discovery tests do not need the SDK or its optional video dependencies.
spec = importlib.util.spec_from_file_location('migration_under_test', EXAMPLES / 'migrate.py')
migration = importlib.util.module_from_spec(spec)
with patch.dict(sys.modules, {'tator': ModuleType('tator')}), patch('logging.basicConfig'):
    spec.loader.exec_module(migration)


def args(**updates):
    parser = argparse.ArgumentParser()
    add_acl_arguments(parser)
    result = parser.parse_args([])
    result.project = 1
    result.dest_organization = 20
    result.skip_sections = False
    result.section_ids = None
    result.version_ids = None
    vars(result).update(updates)
    return result


class API:
    def __init__(self):
        self.orgs, self.groups, self.users, self.rows = {}, {}, {}, {}
        self.affs = {}
        self.writes = []
        self.next_id = 100

    def ident(self):
        self.next_id += 1
        return self.next_id

    def get_project(self, pk):
        return Obj(id=pk, organization=10)

    def get_organization(self, pk):
        return self.orgs[pk]

    def get_organization_list(self):
        return list(self.orgs.values())

    def create_organization(self, organization_spec):
        new = Obj(id=self.ident(), **organization_spec)
        self.orgs[new.id] = new
        self.writes.append(('organization', new.id))
        return new

    def get_group(self, pk):
        return self.groups[pk]

    def get_group_list(self, organization):
        return [g for g in self.groups.values() if g.organization == organization]

    def create_group(self, organization, group_spec):
        new = Obj(id=self.ident(), organization=organization, members=[], **group_spec)
        self.groups[new.id] = new
        self.writes.append(('group', new.id))
        return new

    def update_group(self, pk, group_update_spec):
        self.groups[pk].members.extend(group_update_spec['add_members'])
        self.writes.append(('members', pk))

    def get_user(self, pk):
        return self.users[pk]

    def get_user_list(self, username):
        return [u for u in self.users.values() if u.username == username]

    def get_affiliation_list(self, organization):
        return [a for a in self.affs.values() if a.organization_id == organization]

    def create_affiliation(self, organization, affiliation_spec):
        new = Obj(id=self.ident(), organization_id=organization, user_id=affiliation_spec['user'],
                  permission=affiliation_spec['permission'])
        self.affs[new.id] = new
        self.writes.append(('affiliation', new.id))
        return new

    def get_row_protection_list(self, **filters):
        return [r for r in self.rows.values()
                if all(getattr(r, k, None) == v for k, v in filters.items())]

    def create_row_protection(self, row_protection_spec):
        new = Obj(id=self.ident(), **row_protection_spec)
        self.rows[new.id] = new
        self.writes.append(('rp', new.id))
        return new

    def update_row_protection(self, pk, row_protection_update_spec):
        self.rows[pk].permission = row_protection_update_spec['permission']
        self.writes.append(('rp_update', pk))


class ACLTests(unittest.TestCase):
    def setUp(self):
        self.src, self.dst = API(), API()
        self.src.orgs[10] = Obj(id=10, name='Source')
        self.dst.orgs[20] = Obj(id=20, name='Different destination name')
        self.src.users[1] = Obj(id=1, username='alice')
        self.dst.users[9] = Obj(id=9, username='alice')

    def acl(self, **options):
        acl = ACLMigration(args(**options), self.src, self.dst,
                           {'project': {1: 2}, 'section': {3: 30}, 'version': {4: 40}})
        acl.bind_project_organization(Obj(organization=20))
        return acl

    def row(self, pk, **values):
        self.src.rows[pk] = Obj(id=pk, **values)

    def test_dependency_closure_and_rerun(self):
        self.src.groups[5] = Obj(id=5, organization=10, name='Reviewers', members=[1])
        self.row(1, project=1, group=5, permission=123)
        self.row(2, target_group=5, group=5, permission=7)  # cycle
        self.row(3, target_organization=10, user=1, permission=8)
        self.row(4, project=999, group=5, permission=255)  # same grantee, unrelated target
        first = self.acl().run()
        self.assertEqual(set(first['row_protection']), {1, 2, 3})
        self.assertEqual(len(self.dst.groups), 1)
        self.assertEqual(next(iter(self.dst.groups.values())).members, [9])
        writes = list(self.dst.writes)
        second = self.acl().run()
        self.assertEqual(first['row_protection'], second['row_protection'])
        self.assertEqual(self.dst.writes, writes)

    def test_compound_target_and_zero_mask(self):
        self.row(1, section=3, version=4, user=1, permission=0)
        self.row(2, section=3, version=999, user=1, permission=123)
        mapping = self.acl().run()
        self.assertEqual(set(mapping['row_protection']), {1})
        result = next(iter(self.dst.rows.values()))
        self.assertEqual((result.section, result.version, result.user, result.permission), (30, 40, 9, 0))

    def test_skip_direct_users_keeps_group_members(self):
        self.src.groups[5] = Obj(id=5, organization=10, name='Reviewers', members=[1])
        self.row(1, project=1, user=1, permission=7)
        self.row(2, project=1, group=5, permission=7)
        mapping = self.acl(skip_user_row_protections=True).run()
        self.assertEqual(set(mapping['row_protection']), {2})
        self.assertEqual(next(iter(self.dst.groups.values())).members, [9])

    def test_missing_user_is_reported(self):
        self.dst.users.clear()
        self.row(1, project=1, user=1, permission=7)
        acl = self.acl()
        acl.run()
        self.assertFalse(self.dst.rows)
        self.assertTrue(acl.skipped)

    def test_organization_grantee_copies_all_affiliations(self):
        self.src.affs[6] = Obj(id=6, organization_id=10, user_id=1, permission='Member')
        self.row(1, project=1, organization=10, permission=7)
        mapping = self.acl().run()
        self.assertEqual(mapping['organization'], {10: 20})
        self.assertEqual(next(iter(self.dst.affs.values())).user_id, 9)
        writes = list(self.dst.writes)
        self.acl().run()
        self.assertEqual(writes, self.dst.writes)

    def test_explicit_group_and_organization_overrides(self):
        self.src.orgs[11] = Obj(id=11, name='Another org')
        self.dst.orgs[21] = Obj(id=21, name='Renamed org')
        self.src.groups[5] = Obj(id=5, organization=11, name='Old', members=[])
        self.dst.groups[50] = Obj(id=50, organization=21, name='New', members=[])
        self.row(1, project=1, group=5, permission=7)
        maps = self.acl(map_organization=[(11, 21)], map_group=[(5, 50)]).run()
        self.assertEqual(maps['group'], {5: 50})
        self.assertEqual(maps['organization'][11], 21)

    def test_conflicting_owner_override(self):
        with self.assertRaises(ValueError):
            self.acl(map_organization=[(10, 99)])

    def test_conflicting_destination_owner(self):
        with self.assertRaises(ValueError):
            self.acl(dest_organization=99)

    def test_skip_group_creation_still_reuses_match(self):
        self.src.groups[5] = Obj(id=5, organization=10, name='Reviewers', members=[1])
        self.dst.groups[50] = Obj(id=50, organization=20, name='Reviewers', members=[])
        self.row(1, project=1, group=5, permission=7)
        self.acl(skip_groups=True).run()
        self.assertEqual(next(iter(self.dst.rows.values())).group, 50)
        self.assertEqual(self.dst.groups[50].members, [])

    def test_skip_unmatched_group_reports_dependency(self):
        self.src.groups[5] = Obj(id=5, organization=10, name='Reviewers', members=[])
        self.row(1, project=1, group=5, permission=7)
        acl = self.acl(skip_groups=True)
        acl.run()
        self.assertFalse(self.dst.rows)
        self.assertTrue(acl.skipped)

    def test_skip_row_protections(self):
        self.row(1, project=1, user=1, permission=7)
        self.acl(skip_row_protections=True).run()
        self.assertFalse(self.dst.writes)

    def test_conflict_detected_before_any_rp_write(self):
        self.row(1, project=1, user=1, permission=7)
        self.row(2, section=3, user=1, permission=5)
        self.dst.rows[90] = Obj(id=90, section=30, user=9, permission=255)
        with self.assertRaises(ValueError):
            self.acl().run()
        self.assertFalse(self.dst.writes)
        self.acl(acl_conflicts='source').run()
        self.assertEqual(self.dst.rows[90].permission, 5)

    def test_duplicate_source_rules_are_created_once(self):
        self.row(1, project=1, user=1, permission=7)
        self.row(2, project=1, user=1, permission=7)
        maps = self.acl().run()
        self.assertEqual(maps['row_protection'][1], maps['row_protection'][2])
        self.assertEqual(len(self.dst.rows), 1)

    def test_unselected_override_does_not_expand_scope(self):
        self.acl(map_organization=[(999, 998)], map_group=[(997, 996)]).run()
        self.assertFalse(self.dst.writes)

    def test_group_override_must_belong_to_mapped_org(self):
        self.src.groups[5] = Obj(id=5, organization=10, name='Reviewers', members=[])
        self.dst.groups[50] = Obj(id=50, organization=999, name='Reviewers', members=[])
        self.row(1, project=1, group=5, permission=7)
        with self.assertRaises(ValueError):
            self.acl(map_group=[(5, 50)]).run()

    def test_master_section_mapping(self):
        src_section = Obj(id=3, name='A', path='A', master_section=6)
        src_master = Obj(id=6, name='Master', path='Master', master_section=6)
        dst_section = Obj(id=30, name='A', path='A', master_section=30)
        dst_master = Obj(id=60, name='Master', path='Master', master_section=60)
        self.src.get_section_list = Mock(return_value=[src_section, src_master])
        self.dst.get_section_list = Mock(return_value=[dst_section, dst_master])
        self.src.get_media = Mock(return_value=Obj(master_section=6))
        self.dst.get_media = Mock(return_value=Obj(master_section=30))
        self.dst.update_section, self.dst.update_media = Mock(), Mock()
        acl = self.acl()
        acl.maps['media'] = {7: 70}
        acl.preserve_master_sections(2)
        self.assertEqual(acl.maps['section'][6], 60)
        self.dst.update_section.assert_called_once_with(30, section_update={'master_section': 60})
        self.dst.update_media.assert_called_once_with(70, media_update={'master_section': 60})

    def test_skip_discovery_keeps_existing_media_mapping(self):
        options = args(skip_media=True)
        self.src.get_media_list = Mock(return_value=[Obj(id=7, name='video', attributes={})])
        self.dst.get_media_list = Mock(return_value=[Obj(id=70, name='video', attributes={})])
        self.src.get_section_list = Mock(return_value=[])
        self.dst.get_section_list = Mock(return_value=[])
        pending, mapping = migration.find_media(options, self.src, self.dst, Obj(id=2))
        self.assertEqual(pending, [])
        self.assertEqual(mapping, {7: 70})
        options.skip_acl = True
        self.assertEqual(migration.find_media(options, self.src, self.dst, Obj(id=2)), ([], {}))

    def test_sections_keep_mapping_when_skipped(self):
        self.src.get_section_list = Mock(return_value=[Obj(id=3, name='A', path='A')])
        self.dst.get_section_list = Mock(return_value=[Obj(id=30, name='A', path='A')])
        pending, mapping = migration.find_sections(args(skip_sections=True), self.src, self.dst, Obj(id=2))
        self.assertEqual((pending, mapping), ([], {3: 30}))

    def test_creates_cross_organization_dependencies(self):
        self.src.orgs[11] = Obj(id=11, name='External team')
        self.src.groups[5] = Obj(id=5, organization=11, name='Reviewers', members=[1])
        self.row(1, project=1, group=5, permission=7)
        maps = self.acl().run()
        self.assertNotEqual(maps['organization'][11], 20)
        self.assertEqual(self.dst.groups[maps['group'][5]].organization, maps['organization'][11])
        writes = list(self.dst.writes)
        self.acl().run()
        self.assertEqual(writes, self.dst.writes)

    def test_unsupported_direct_annotation_rule_is_reported(self):
        self.row(1, localization=88, user=1, permission=7)
        acl = self.acl()
        acl.maps['localization'] = {88: 888}
        acl.run()
        self.assertFalse(self.dst.rows)
        self.assertIn('unsupported targets', acl.skipped[0])

    def test_skip_rps_still_selects_groups(self):
        self.src.groups[5] = Obj(id=5, organization=10, name='Reviewers', members=[1])
        self.row(1, project=1, group=5, permission=7)
        maps = self.acl(skip_row_protections=True).run()
        self.assertIn(5, maps['group'])
        self.assertFalse(self.dst.rows)

    def test_skip_affiliations(self):
        self.src.affs[6] = Obj(id=6, organization_id=10, user_id=1, permission='Member')
        self.row(1, project=1, organization=10, permission=7)
        self.acl(skip_affiliations=True).run()
        self.assertFalse(self.dst.affs)
        self.assertEqual(next(iter(self.dst.rows.values())).organization, 20)

    def test_memberships_match_existing_destination_users(self):
        source_membership = Obj(id=6, user=1, permission='View Only')
        self.dst.get_membership_list = Mock(return_value=[])
        self.dst.create_membership = Mock(return_value=Obj(id=60))
        members, users = {}, {}
        migration.create_memberships(self.src, self.dst, 2, [source_membership],
                                     [self.src.users[1]], members, users)
        self.assertEqual(members, {6: 60})
        self.assertEqual(users, {1: 9})
        self.dst.create_membership.assert_called_once_with(
            2, membership_spec={'user': 9, 'permission': 'View Only'})

    def test_script_existing_project_acl_pass_and_rerun(self):
        options = args(dest_project=2, skip_memberships=True, ignore_media_transfer=False)
        for kind in ('media', 'versions', 'media_types', 'localization_types', 'state_types',
                     'leaf_types', 'file_types', 'localizations', 'states', 'leaves'):
            setattr(options, 'skip_' + kind, True)
        for api in (self.src, self.dst):
            for kind in ('membership', 'section', 'version', 'media_type', 'localization_type',
                         'state_type', 'leaf_type', 'file_type', 'media', 'leaf'):
                setattr(api, 'get_' + kind + '_list', Mock(return_value=[]))
        self.dst.get_project = Mock(return_value=Obj(id=2, name='Destination', organization=20))
        self.row(1, project=1, user=1, permission=7)
        with patch.object(migration, 'setup_apis', return_value=(self.src, self.dst)), \
                patch('builtins.input', return_value='y'):
            first = migration.migrate(options)
            writes = list(self.dst.writes)
            second = migration.migrate(options)
        self.assertEqual(first['row_protection'], second['row_protection'])
        self.assertEqual(first['project'], {1: 2})
        self.assertEqual(writes, self.dst.writes)

    def test_duplicate_override_rejected(self):
        with self.assertRaises(ValueError):
            self.acl(map_group=[(1, 2), (1, 3)])

    def test_acl_enabled_by_default_and_explicitly_skippable(self):
        parser = argparse.ArgumentParser()
        add_acl_arguments(parser)
        self.assertFalse(parser.parse_args([]).skip_acl)
        self.assertTrue(parser.parse_args(['--skip_acl']).skip_acl)

    def test_skipped_new_project_resources_do_not_scan_source(self):
        source, destination = Mock(), Mock()
        kinds = ('media', 'localizations', 'states', 'sections', 'versions',
                 'media_types', 'localization_types', 'state_types', 'leaf_types',
                 'file_types', 'leaves')
        for kind in kinds:
            with self.subTest(kind=kind):
                options = args(**{'skip_' + kind: True})
                pending, mapping = getattr(migration, 'find_' + kind)(
                    options, source, destination, None)
                self.assertFalse(pending)
                self.assertEqual(mapping, {})
        self.assertFalse(source.mock_calls)
        self.assertFalse(destination.mock_calls)

    def test_mapping_only_discovery_never_announces_creation(self):
        self.src.get_media_list = Mock(return_value=[Obj(id=7, name='video', attributes={})])
        self.dst.get_media_list = Mock(return_value=[])
        self.src.get_section_list = Mock(return_value=[])
        self.dst.get_section_list = Mock(return_value=[])
        with self.assertLogs(migration.logger, level='INFO') as logs:
            pending, mapping = migration.find_media(args(skip_media=True), self.src, self.dst, Obj(id=2))
        self.assertEqual((pending, mapping), ([], {}))
        self.assertNotIn('will be created', ' '.join(logs.output))
        self.assertIn('Skipping creation of media', ' '.join(logs.output))

    def test_membership_plan_excludes_missing_users_and_creator(self):
        self.src.users.update({pk: Obj(id=pk, username=f'user{pk}') for pk in range(2, 76)})
        self.src.get_membership_list = Mock(return_value=[
            Obj(id=pk, user=pk, permission='View Only') for pk in range(1, 76)])
        self.dst.whoami = Mock(return_value=self.dst.users[9])
        with self.assertLogs(migration.logger, level='INFO') as logs:
            pending, users, members, user_map = migration.find_memberships(
                args(skip_memberships=False), self.src, self.dst, None)
        self.assertEqual(len(pending), 1)  # Map the automatic creator membership after creation.
        self.assertEqual(user_map, {1: 9})
        self.assertIn('0 memberships will be created', ' '.join(logs.output))
        self.assertIn('1 supplied by project creation', ' '.join(logs.output))
        self.assertIn('74 skipped: no matching destination user', ' '.join(logs.output))

    def test_membership_plan_includes_existing_account_not_yet_in_project(self):
        self.src.get_membership_list = Mock(return_value=[Obj(id=6, user=1, permission='View Only')])
        self.dst.get_membership_list = Mock(return_value=[])
        with self.assertLogs(migration.logger, level='INFO') as logs:
            pending, users, members, user_map = migration.find_memberships(
                args(skip_memberships=False), self.src, self.dst, Obj(id=2))
        self.assertEqual([m.id for m in pending], [6])
        self.assertEqual(user_map, {1: 9})
        self.assertIn('1 memberships will be created', ' '.join(logs.output))

    def preview(self, acl, pending=None, dest_project=None):
        return acl.preview(dest_project, {'section': {}, 'version': {}}, pending or {})

    def test_preview_counts_dependencies_without_writes_or_map_changes(self):
        self.src.orgs[11] = Obj(id=11, name='External team')
        self.src.groups[5] = Obj(id=5, organization=11, name='Reviewers', members=[1])
        self.src.affs[6] = Obj(id=6, organization_id=11, user_id=1, permission='Member')
        self.row(1, project=1, group=5, permission=7)
        self.row(2, target_group=5, user=1, permission=3)
        acl = self.acl()
        before = {kind: dict(ids) for kind, ids in acl.maps.items()}
        with self.assertLogs('migrate_acl', level='INFO') as logs:
            counts = self.preview(acl)
        self.assertEqual(counts['organizations']['create'], 1)
        self.assertEqual(counts['organizations']['existing'], 1)
        self.assertEqual(counts['groups']['create'], 1)
        self.assertEqual(counts['group memberships']['create'], 1)
        self.assertEqual(counts['affiliations']['create'], 1)
        self.assertEqual(counts['row protections']['create'], 2)
        self.assertIn('2 row protections will be created', ' '.join(logs.output))
        self.assertFalse(self.dst.writes)
        self.assertEqual(dict(acl.maps), before)
        self.assertEqual(self.dst.orgs.keys(), {20})
        self.assertEqual(acl.args.dest_organization, 20)

    def test_preview_existing_acl_counts_no_creates(self):
        self.src.groups[5] = Obj(id=5, organization=10, name='Reviewers', members=[1])
        self.row(1, project=1, group=5, permission=7)
        self.acl().run()
        writes = list(self.dst.writes)
        counts = self.preview(self.acl(), dest_project=Obj(id=2))
        self.assertEqual(counts['groups']['create'], 0)
        self.assertEqual(counts['groups']['existing'], 1)
        self.assertEqual(counts['group memberships']['existing'], 1)
        self.assertEqual(counts['row protections']['create'], 0)
        self.assertEqual(counts['row protections']['existing'], 1)
        self.assertEqual(writes, self.dst.writes)

    def test_preview_selects_pending_compound_targets(self):
        self.row(1, section=3, version=4, user=1, permission=0)
        self.src.get_section_list = Mock(return_value=[Obj(id=3, master_section=3)])
        pending = {'section': [Obj(id=3)], 'version': [Obj(id=4)]}
        counts = self.preview(self.acl(), pending)
        self.assertEqual(counts['row protections']['create'], 1)
        self.assertFalse(self.dst.writes)

    def test_preview_counts_skipped_user_rps(self):
        self.row(1, project=1, user=1, permission=7)
        counts = self.preview(self.acl(skip_user_row_protections=True))
        self.assertEqual(counts['row protections']['create'], 0)
        self.assertEqual(counts['row protections']['skipped'], 1)
        self.assertFalse(self.dst.writes)

    def test_preview_conflicts_stop_before_writes(self):
        self.row(1, project=1, user=1, permission=7)
        self.dst.rows[90] = Obj(id=90, project=2, user=9, permission=255)
        with self.assertLogs('migrate_acl', level='INFO') as logs:
            with self.assertRaisesRegex(ValueError, 'Resolve ACL conflicts'):
                self.preview(self.acl(), dest_project=Obj(id=2))
        self.assertIn('1 conflicts', ' '.join(logs.output))
        self.assertEqual(self.dst.rows[90].permission, 255)
        self.assertFalse(self.dst.writes)
        counts = self.preview(self.acl(acl_conflicts='source'), dest_project=Obj(id=2))
        self.assertEqual(counts['row protections']['update'], 1)
        self.assertEqual(self.dst.rows[90].permission, 255)
        self.assertFalse(self.dst.writes)

    def test_cancelled_script_previews_acl_without_writes(self):
        options = args(dest_project=2, skip_memberships=True, ignore_media_transfer=False)
        for kind in ('media', 'versions', 'media_types', 'localization_types', 'state_types',
                     'leaf_types', 'file_types', 'localizations', 'states', 'leaves'):
            setattr(options, 'skip_' + kind, True)
        for api in (self.src, self.dst):
            for kind in ('membership', 'section', 'version', 'media_type', 'localization_type',
                         'state_type', 'leaf_type', 'file_type', 'media', 'leaf'):
                setattr(api, 'get_' + kind + '_list', Mock(return_value=[]))
        self.dst.get_project = Mock(return_value=Obj(id=2, name='Destination', organization=20))
        self.src.groups[5] = Obj(id=5, organization=10, name='Reviewers', members=[1])
        self.row(1, project=1, group=5, permission=7)
        events = []
        self.dst.get_row_protection_list = Mock(side_effect=lambda **kw: events.append('preview') or [])
        with patch.object(migration, 'setup_apis', return_value=(self.src, self.dst)), \
                patch('builtins.input', side_effect=lambda prompt: events.append('confirm') or 'n'):
            migration.migrate(options)
        self.assertEqual(events, ['preview', 'confirm'])
        self.assertFalse(self.dst.writes)
        self.assertFalse(self.dst.groups)

    def test_version_selection_includes_bases_first(self):
        versions = [Obj(id=4, bases=[2]), Obj(id=8, bases=[]), Obj(id=2, bases=[1]), Obj(id=1, bases=[])]
        self.assertEqual([v.id for v in migration.select_versions(versions, [4])], [1, 2, 4])
        with self.assertRaisesRegex(ValueError, 'not found'):
            migration.select_versions(versions, [99])
        with self.assertRaisesRegex(ValueError, 'Cycle'):
            migration.select_versions([Obj(id=4, bases=[4])], [4])

    def test_version_skip_still_maps_only_selected_definitions(self):
        self.src.get_version_list = Mock(return_value=[
            Obj(id=4, name='Selected', bases=[]), Obj(id=8, name='Other', bases=[])])
        self.dst.get_version_list = Mock(return_value=[
            Obj(id=40, name='Selected'), Obj(id=80, name='Other')])
        pending, maps = migration.find_versions(args(version_ids=[4], skip_versions=True),
                                               self.src, self.dst, Obj(id=2))
        self.assertEqual((pending, maps), ([], {4: 40}))

    def test_section_selection_uses_path_components(self):
        sections = [Obj(id=1, name='A', path='A'), Obj(id=3, name='B', path='A.B'),
                    Obj(id=4, name='Child', path='A.B.C'), Obj(id=5, name='Beta', path='A.Beta')]
        self.src.get_section_list = Mock(return_value=sections)
        selected = migration.get_section_list_from_ids(self.src, args(section_ids=[3]))
        self.assertEqual([s.id for s in selected], [1, 3, 4])
        with self.assertRaisesRegex(ValueError, 'not found'):
            migration.get_section_list_from_ids(self.src, args(section_ids=[99]))

    def test_annotation_selection_filters_versions_in_queries_and_mappings(self):
        for kind in ('localization', 'state'):
            with self.subTest(kind=kind):
                src_media, dst_media = (7, 70) if kind == 'localization' else ([7], [70])
                source_objects = [Obj(id=1, media=src_media, frame=0, version=4),
                                  Obj(id=2, media=src_media, frame=0, version=8),
                                  Obj(id=3, media=src_media, frame=0, version=2)]  # base definition only
                getter = Mock(return_value=source_objects)
                setattr(self.src, 'get_' + kind + '_list', getter)
                setattr(self.dst, 'get_' + kind + '_list', Mock(return_value=[
                    Obj(id=10, media=dst_media, frame=0, version=40)]))
                options = args(version_ids=[4], **{'skip_' + kind + 's': False})
                with patch.object(migration, '_same_' + kind,
                                  side_effect=lambda a, b, *maps: a.version == 4 and b.version == 40):
                    pending, maps = getattr(migration, 'find_' + kind + 's')(
                        options, self.src, self.dst, Obj(id=2), [], {7: 70}, {}, {4: 40, 2: 20})
                self.assertEqual((pending, maps), ([], {1: 10}))
                getter.assert_called_once_with(1, media_id=[7], version=[4])

    def test_states_crossing_section_selection_are_not_cloned(self):
        self.src.get_state_list = Mock(return_value=[Obj(id=1, media=[7, 8], frame=0, version=4)])
        self.dst.get_state_list = Mock(return_value=[])
        pending, maps = migration.find_states(args(version_ids=[4], skip_states=False),
                                              self.src, self.dst, Obj(id=2), [], {7: 70}, {}, {4: 40})
        self.assertEqual((pending, maps), ([], {}))

    def test_section_and_version_selection_scope_preview_and_copied_rps(self):
        sections = [Obj(id=3, name='Selected', path='Selected', master_section=3),
                    Obj(id=5, name='Other', path='Other', master_section=5)]
        self.src.get_section_list = Mock(return_value=sections)
        self.dst.get_section_list = Mock(return_value=[
            Obj(id=30, name='Selected', path='Selected', master_section=30),
            Obj(id=50, name='Other', path='Other', master_section=50)])
        self.src.get_version_list = Mock(return_value=[
            Obj(id=4, name='Selected', bases=[]), Obj(id=8, name='Other', bases=[])])
        self.dst.get_version_list = Mock(return_value=[Obj(id=40, name='Selected'), Obj(id=80, name='Other')])
        options = args(section_ids=[3], version_ids=[4], skip_sections=True, skip_versions=True)
        _, sections_map = migration.find_sections(options, self.src, self.dst, Obj(id=2))
        _, versions_map = migration.find_versions(options, self.src, self.dst, Obj(id=2))
        self.row(1, project=1, user=1, permission=7)
        self.row(2, section=3, user=1, permission=7)
        self.row(3, version=4, user=1, permission=7)
        self.row(4, section=3, version=4, user=1, permission=7)
        self.row(5, section=5, version=4, group=999, permission=7)
        self.row(6, section=3, version=8, group=999, permission=7)
        self.row(7, version=8, group=999, permission=7)
        self.row(8, section=5, group=999, permission=7)
        acl = self.acl(section_ids=[3], version_ids=[4])
        maps = {'section': sections_map, 'version': versions_map}
        counts = acl.preview(Obj(id=2), maps, {})
        self.assertEqual(counts['row protections']['create'], 4)
        self.assertEqual(counts['groups']['create'], 0)
        self.assertFalse(self.dst.writes)
        acl.maps.update(maps)
        result = acl.run()
        self.assertEqual(set(result['row_protection']), {1, 2, 3, 4})
        self.assertFalse(self.dst.groups)

    def test_version_and_section_cli_ids(self):
        with patch.object(sys, 'argv', ['migrate.py', '--host', 'source', '--token', 'test',
                                       '--project', '1', '--version_ids', '4', '8', '--section_ids', '3']):
            options = migration.parse_args()
        self.assertEqual(options.version_ids, [4, 8])
        self.assertEqual(options.section_ids, [3])

    def test_affiliations_use_schema_user_id_on_both_hosts(self):
        # The dynamic SDK returns None for absent properties, as in the reported traceback.
        self.src.affs[6] = Obj(id=6, organization_id=10, user_id=1, user=None, permission='Member')
        self.dst.affs[60] = Obj(id=60, organization_id=20, user_id=9, user=None, permission='Member')
        self.src.get_user = Mock(wraps=self.src.get_user)
        acl = self.acl()
        maps = acl.run()
        self.assertEqual(maps['affiliation'], {6: 60})
        self.src.get_user.assert_called_once_with(1)
        self.assertFalse(self.dst.writes)

    def test_missing_affiliation_user_id_never_requests_user_none(self):
        self.src.affs[6] = Obj(id=6, organization_id=10, user_id=None, permission='Member')
        self.src.get_user = Mock(side_effect=AssertionError('Must not fetch a missing user ID'))
        acl = self.acl()
        acl.run()
        self.src.get_user.assert_not_called()
        self.assertEqual(acl.counts['affiliations']['skipped'], 1)
        self.assertFalse(self.dst.writes)

    def test_missing_user_logs_are_summarized(self):
        self.dst.users.clear()
        for pk in range(1, 76):
            self.src.users[pk] = Obj(id=pk, username=f'missing{pk}@example.com')
            self.row(pk, project=1, user=pk, permission=7)
        with self.assertLogs('migrate_acl', level='INFO') as logs:
            counts = self.preview(self.acl())
        output = '\n'.join(logs.output)
        self.assertIn('0 row protections will be created (0 already exist, 75 skipped).', output)
        self.assertIn('ACL users: 0 matched, 75 skipped (no matching destination username).', output)
        self.assertNotIn('@example.com', output)
        self.assertNotIn('unresolved user grantee', output)
        self.assertLessEqual(len(logs.output), 7)
        self.assertEqual(counts['row protections']['skipped'], 75)
        self.assertFalse(self.dst.writes)

    def test_per_object_diagnostics_are_debug_level(self):
        self.dst.users.clear()
        with self.assertLogs('migrate_acl', level='DEBUG') as logs:
            self.acl().user(1)
        self.assertTrue(all(record.levelname == 'DEBUG' for record in logs.records))
        self.assertIn('No destination user', logs.output[0])

    def test_acl_user_summary_includes_previously_matched_users(self):
        self.row(1, project=1, user=1, permission=7)
        self.src.users[2] = Obj(id=2, username='missing')
        self.row(2, project=1, user=2, permission=7)
        acl = self.acl()
        acl.maps['user'][1] = 9  # Matched during project membership discovery.
        with self.assertLogs('migrate_acl', level='INFO') as logs:
            counts = self.preview(acl)
        self.assertIn('ACL users: 1 matched, 1 skipped', '\n'.join(logs.output))
        self.assertEqual(counts['row protections']['create'], 1)

    def test_existing_organization_rp_conflict_is_explained_for_new_project(self):
        self.row(10, target_organization=10, user=1, permission=7)
        self.dst.rows[90] = Obj(id=90, target_organization=20, user=9, permission=255)
        with self.assertLogs('migrate_acl', level='INFO') as logs:
            with self.assertRaisesRegex(ValueError, 'Resolve ACL conflicts'):
                self.preview(self.acl())
        output = '\n'.join(logs.output)
        self.assertIn('source RP 10 [target_organization=10, user=1] (mask=0x7)', output)
        self.assertIn('destination [target_organization=20, user=9]', output)
        self.assertIn('90 (mask=0xff)', output)
        self.assertIn('--acl_conflicts source', output)
        self.assertFalse(self.dst.writes)

    def test_conflicting_source_rules_are_distinguished_from_destination_conflicts(self):
        self.row(10, project=1, user=1, permission=7)
        self.row(11, project=1, user=1, permission=255)
        with self.assertLogs('migrate_acl', level='INFO') as logs:
            with self.assertRaisesRegex(ValueError, 'Resolve ACL conflicts'):
                self.preview(self.acl(acl_conflicts='source'))
        output = '\n'.join(logs.output)
        self.assertIn('source RPs 10 (mask=0x7) and 11 (mask=0xff)', output)
        self.assertIn('project=new (source IDs [1])', output)
        self.assertIn('cannot choose between conflicting source rules', output)
        self.assertIn('0 row protections will be created (0 already exist, 1 conflicts).', output)
        self.assertFalse(self.dst.writes)

    def test_destination_policy_keeps_org_rp_and_creates_missing_rules(self):
        self.row(1, target_organization=10, user=1, permission=7)
        self.row(2, project=1, user=1, permission=3)
        self.dst.rows[90] = Obj(id=90, target_organization=20, user=9, permission=255)
        acl = self.acl(acl_conflicts='destination')
        counts = self.preview(acl, dest_project=Obj(id=2))
        self.assertEqual(counts['row protections']['existing'], 1)
        self.assertEqual(counts['row protections']['retained'], 1)
        self.assertEqual(counts['row protections']['update'], 0)
        self.assertEqual(counts['row protections']['create'], 1)
        maps = acl.run()
        self.assertEqual(maps['row_protection'][1], 90)
        self.assertEqual(self.dst.rows[90].permission, 255)
        self.assertEqual(self.dst.rows[maps['row_protection'][2]].permission, 3)
        writes = list(self.dst.writes)
        self.acl(acl_conflicts='destination').run()
        self.assertEqual(writes, self.dst.writes)
        self.assertFalse(any(action == 'rp_update' for action, pk in writes))

    def test_destination_policy_keeps_all_duplicate_existing_rules(self):
        self.row(1, project=1, user=1, permission=7)
        self.row(2, project=1, user=1, permission=3)
        self.dst.rows[90] = Obj(id=90, project=2, user=9, permission=255)
        self.dst.rows[91] = Obj(id=91, project=2, user=9, permission=15)
        self.acl(acl_conflicts='destination').run()
        self.assertFalse(self.dst.writes)
        self.assertEqual(self.dst.rows[90].permission, 255)
        self.assertEqual(self.dst.rows[91].permission, 15)

    def test_destination_policy_rejects_ambiguous_source_without_destination(self):
        self.row(1, project=1, user=1, permission=7)
        self.row(2, project=1, user=1, permission=3)
        with self.assertRaisesRegex(ValueError, 'existing destination rule'):
            self.acl(acl_conflicts='destination').run()
        self.assertFalse(self.dst.writes)

    def test_destination_policy_cli(self):
        parser = argparse.ArgumentParser()
        add_acl_arguments(parser)
        self.assertEqual(parser.parse_args(['--acl_conflicts', 'destination']).acl_conflicts, 'destination')

    def test_cli_repeated_mapping(self):
        parser = argparse.ArgumentParser()
        add_acl_arguments(parser)
        parsed = parser.parse_args(['--map_group', '1:2', '--map_group', '3:4',
                                    '--skip_user_row_protections'])
        self.assertEqual(parsed.map_group, [(1, 2), (3, 4)])
        self.assertTrue(parsed.skip_user_row_protections)


if __name__ == '__main__':
    unittest.main()
