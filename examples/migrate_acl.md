# Migrating project ACLs

By default, `migrate.py` copies the permission structures used by migrated data.
Use `--skip_acl` to disable all ACL migration. Keep `migrate_acl.py`
alongside `migrate.py` when copying the example scripts elsewhere.

For example, migrate into an existing project, omitting direct user grants:

```sh
python examples/migrate.py \
  --host "$SOURCE_HOST" --token "$SOURCE_TOKEN" --project 1 \
  --dest_host "$DEST_HOST" --dest_token "$DEST_TOKEN" --dest_project 200 \
  --skip_user_row_protections
```

For a new project in a differently named destination organization, use
`--new_project_name 'Cloned project' --dest_organization 20` in place of
`--dest_project 200`. The source project's owning organization maps to organization
20 regardless of its name. An existing destination project's organization takes
precedence; contradictory organization options are rejected.

Additional renamed dependencies can be mapped with repeatable options:

```sh
--map_organization 11:21 --map_group 5:50 --map_group 6:60
```

IDs are `SOURCE_ID:DEST_ID`. A group override must belong to its mapped
organization. Overrides only apply to selected dependencies; they do not select
otherwise unrelated objects. Organizations otherwise match by name; groups match
by name within the mapped organization. Ambiguous matches require an override.

## Selection and mappings

Mappings stay in memory. The existing discovery rules identify prior copies, and
newly created IDs extend those mappings. With ACL migration enabled, data skip
flags skip creation but still discover existing matches in an existing destination
project. For a new destination project, skipped resources are not scanned because
there cannot be any existing matches. The same command can
add ACLs to previously migrated data. `migrate(args)` returns the complete mapping
by object kind for callers importing the script; no manifest is written.

The selected project, sections, versions, media, and other mapped objects seed ACL
selection. Their RPs select grantee groups/organizations, owning organizations,
and the RPs protecting those ACL objects, recursively. Unrelated data accessible
to the same group is not selected. Section/version rules require both mappings.
Master-section references are preserved, including required master sections outside
`--section_ids`; if a required section is missing and `--skip_sections` is set,
the migration fails instead of assigning a different ACL origin.

Selected groups receive missing members. Selected organizations receive missing
affiliations, including members without project membership. Users are matched by
username and are **never created**. Missing users and their dependent grants or
memberships are reported and skipped. Group membership record IDs/admin-role
metadata are not exposed by the group API; only member user IDs can be copied.

## Selecting sections and versions

Use `--section_ids 3 5` and `--version_ids 4 8` together or independently.
Section selection includes the specified sections, their ancestors, and their
descendants, using complete dot-separated path components. Unknown selected IDs
are rejected when their resource discovery runs.

Version selection includes only the requested versions' annotations. Required
base version **definitions** are also mapped or created, in dependency order, to
preserve version inheritance; their annotations are not implicitly selected.
Without `--version_ids`, all source versions and annotations remain eligible.
With both flags, annotations must belong to the selected media and explicitly
requested versions. States referencing media outside the selected set are
reported and skipped rather than pulling in unselected media.

The same scoped mappings drive the ACL preview and execution. Section-only and
version-only RPs are eligible only for mapped selected targets or required
inheritance dependencies. A compound section/version RP requires both targets.
Excluded rules do not select their grantee groups or organizations. Project-level
and organization-level rules providing inherited access remain eligible.
The filters apply to discovery of previously migrated objects as well as creation,
so existing destination objects outside the selection do not widen ACL scope.

## Preview before confirmation

Before `Continue with migration [y/N]?`, the script prints ACL counts for
organizations, groups, group memberships, affiliations, row protections, and
additional master sections required by ACL inheritance. Each resource gets one
line showing how many will be created and already exist; nonzero update, skip,
and conflict counts are appended. Disabled affiliation copying is explicitly
labeled. The user summary reports both matched and missing usernames across all
selected ACL dependencies, including organization affiliations and group members;
this population can be larger than the project membership list. Per-object diagnostics are written
to `migrate.log` at DEBUG level instead of printing on the console.

The preview includes both previously migrated resources and resources scheduled
for creation. It follows the same dependencies and matches destination users,
groups, organizations, and RPs as execution. It makes no destination writes;
cancelling at the prompt also leaves ACL structures unchanged. Known RP conflicts
are reported before confirmation and stop the migration under the default policy.
Each conflict identifies the source/destination RP IDs, targets, grantee, and
permission masks. Destination mask conflicts can be overridden with
`--acl_conflicts source`, or retained with `--acl_conflicts destination`.
Conflicting source rules require an existing destination rule to retain; otherwise
the source rules or mappings must be resolved separately. A new project can still have conflicts on an existing mapped organization.

Counts describe planned explicit copies against the current destination. Server
creation operations can generate default RPs or affiliations, and concurrent
changes can affect the final counts. The execution phase rechecks those objects
and reuses them instead of creating duplicates.

## Controls and conflicts

- `--skip_acl`: disable ACL dependency discovery and copying entirely. Legacy
  project memberships remain controlled by `--skip_memberships`.
- `--skip_organizations`: reuse mapped/matched organizations but do not create them.
- `--skip_groups`: reuse mapped/matched groups but do not create groups or add members.
- `--skip_affiliations`: do not copy organization affiliations.
- `--skip_row_protections`: discover dependencies and copy selected structures,
  but do not copy RPs.
- `--skip_user_row_protections`: omit direct user-grantee RPs. Group/organization
  grants and their memberships remain eligible.
- `--skip_memberships`: skip legacy project membership creation independently.

RP identity comprises all targets and the grantee. Identical masks reuse existing
RPs, including those generated by the server during creation. Different masks
stop the RP phase by default; `--acl_conflicts source` explicitly permits updating
those destination masks. `--acl_conflicts destination` instead preserves existing
destination masks and maps source RPs to those existing rules; missing RPs are
still created. The preview reports differing destination masks retained. Zero masks and full integer masks are preserved. Source
rules that collapse onto the same destination identity with different masks are
rejected unless `destination` policy can retain an existing destination rule. Existing affiliation permission differences are reported, not overwritten.
No destination memberships or unrelated rules are deleted.

New organizations use zero-trust permissions and no default project membership
grant. Existing organization settings are retained. Server-generated creator RPs
and legacy membership/affiliation side effects are not suppressed by
`--skip_user_row_protections`; use the relevant membership skip flags when needed.
Additional destination grants can therefore make effective access differ from the
source, even after all selected source rules have been copied.

The tokens must be able to administer ACLs on the selected targets and access the
required groups, users, and affiliations. Organization creation also requires the
server's organization-creation privilege. RP lists are permission-filtered, so the
script cannot prove completeness when the source token lacks ACL visibility.
Unsupported direct localization/state RPs are reported; their section/version
rules are supported. Files, algorithms, buckets, job clusters, and templates are
not newly cloned by this script.

## Offline tests

From the Python package directory:

```sh
python -m unittest discover -s test/examples -p test_migrate_acl.py
```
