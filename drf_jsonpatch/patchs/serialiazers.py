import ast

import rest_framework.serializers as module_to_patch

from drf_jsonpatch.patcher import Patcher
from drf_jsonpatch.nodes.serialiazers import import_jsonpatch, if_apply_jsonpatch


patch = Patcher(module_to_patch)


# ---- import jsonpatch ----
# added between django imports and drf (just for the beauty)
patch.tree.body.insert(13, import_jsonpatch)


# ---- if isinstance(data, JsonPatch): ----
# Must be added in BaseSerializer.__init__
# before `self.initial_data`'s assignment

# Get class's node
BaseSerializer = None
for branch in patch.tree.body:
    if isinstance(branch, ast.ClassDef) and branch.name == "BaseSerializer":
        BaseSerializer = branch
        break
else:
    raise ValueError("Can't find BaseSerialiser")

# Get __init__'s node
init_method = None
for branch in BaseSerializer.body:
    if isinstance(branch, ast.FunctionDef) and branch.name == "__init__":
        init_method = branch
        break
else:
    raise ValueError("Can't find BaseSerialiser.__init__")

# Add the if condition at the begining of the __init__'s body
init_method.body.insert(0, if_apply_jsonpatch)

patch.apply()
