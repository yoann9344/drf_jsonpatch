import ast
import inspect

from django.conf import settings

settings.configure(DEBUG=True)


def source(o):
    s = inspect.getsource(o).split("\n")
    indent = len(s[0]) - len(s[0].lstrip())
    return "\n".join(i[indent:] for i in s)


def dump_module(module):
    tree = ast.parse(source(module))
    return ast.dump(tree)


def dump_code(code: str):
    tree = ast.parse(code)
    return ast.dump(tree)


if __name__ == "__main__":
    import rest_framework.parsers as drf_parsers
    import rest_framework.serializers as drf_serializers

    from drf_jsonpatch.code.parser import import_jsonpatch, class_JSONPatchParser
    from drf_jsonpatch.code.serialiazers import if_apply_jsonpatch

    # print(dump_code(import_jsonpatch))
    # print(dump_code(class_JSONPatchParser))
    # print(dump_code(if_apply_jsonpatch))
    print(dump_module(drf_parsers))
    # print(dump_module(drf_serializers))
