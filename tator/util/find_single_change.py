from __future__ import annotations
import logging
from typing import Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    import tator.TatorApi

from tator.openapi.tator_openapi import ChangeLog, ChangeLogDescriptionOfChangeNew

logger = logging.getLogger(__name__)


def find_single_change(
    api: tator.TatorApi,
    project_id: int,
    entity_id: int,
    field_name: str,
    old_value: Optional[Any] = None,
    new_value: Optional[Any] = None,
    find_last_change: bool = False,
) -> Optional[ChangeLog]:
    """Finds the ChangeLog containing the desired field/value combination.

    Example:

    .. code-block:: python

        api = tator.get_api(host, token)
        change_log = tator.util.find_change(api, media_id, "_deleted", new_value=True)
        print(change_log)

    At least one of `old_value` and `new_value` must be specified; if both are specified, then the
    matching changelog must match both, not just one.

    The `field_name` must be prefixed with an underscore if it is not a user-defined attribute, note
    how "_deleted" corresponds to the `Media.deleted` field.

    :param api: :class:`tator.TatorApi` object.
    :type api: tator.TatorApi
    :param project_id: Unique integer identifying a project in tator.
    :type project_id: int
    :param entity_id: Unique integer identifying an entity with tracked changes, must identify a
                      leaf, localization, media, or state.
    :type entity_id: int
    :param field_name: The name of the field in which to look for the change(s).
    :type field_name: str
    :param old_value: [Optional] The desired old value to find
    :type old_value: Optional[Any]
    :param new_value: [Optional] The desired new value to find
    :type new_value: Optional[Any]
    :param find_last_change: If True, finds the last matching ChangeLog, otherwise finds the first.
    :type find_last_change: bool
    :returns: The changelog corresponding to the desired value(s) to find or `None` if no matches
              are found.
    :rtype: Optional[ChangeLog]
    """
    if old_value is None and new_value is None:
        raise ValueError(
            "Must specify at least one of the following arguments: [old_value, new_value]"
        )

    change_log_list = api.get_change_log_list(project_id, entity_id=entity_id)

    def change_log_is_a_match(cl):
        matches = True

        if old_value is not None:
            old_change = ChangeLogDescriptionOfChangeNew(name=field_name, value=old_value)
            matches = matches and old_change in cl.description_of_change.old

        if new_value is not None:
            new_change = ChangeLogDescriptionOfChangeNew(name=field_name, value=new_value)
            matches = matches and new_change in cl.description_of_change.new

        return matches

    if find_last_change:
        change_log_list = reversed(change_log_list)
    return next((cl for cl in change_log_list if change_log_is_a_match(cl)), None)
