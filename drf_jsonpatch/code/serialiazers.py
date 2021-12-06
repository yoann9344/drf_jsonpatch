import_apply_json_patch = """
from drf_jsonpatch import apply_json_patch
"""
import_jsonpatch = """
import jsonpatch
"""


# Must be added in BaseSerializer.__init__
# before `self.initial_data`'s assignment
if_apply_jsonpatch = """
if isinstance(data, JsonPatch):
    # serialise current instance to get a dict
    instance_serialized = self.__class__(instance).data
    data = apply_json_patch(patch=data, current_state=instance_serialized)
"""
