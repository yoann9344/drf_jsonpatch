import rest_framework.parsers as module_to_patch

from drf_jsonpatch.patcher import Patcher
from drf_jsonpatch.nodes.parser import import_jsonpatch, class_JSONPatchParser


patch = Patcher(module_to_patch)

# ---- import jsonpatch ----
# added between django imports and drf (just for the beauty)
patch.tree.body.insert(10, import_jsonpatch)

# ---- class JSONPatchParser ----
# must be added after JSONParser, so at the end it is pretty fine
patch.tree.body.append(class_JSONPatchParser)
patch.apply()
