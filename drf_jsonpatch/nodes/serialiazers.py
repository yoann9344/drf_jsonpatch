from ast import (
    Assign,
    Attribute,
    Call,
    If,
    Import,
    ImportFrom,
    Load,
    Name,
    Store,
    alias,
    keyword,
)


import_apply_json_patch = ImportFrom(
    module="drf_jsonpatch",
    names=[alias(name="apply_json_patch")],
    level=0,
)
import_jsonpatch = Import(names=[alias(name="jsonpatch")])


if_apply_jsonpatch = If(
    test=Call(
        func=Name(id="isinstance", ctx=Load()),
        args=[Name(id="data", ctx=Load()), Name(id="JsonPatch", ctx=Load())],
        keywords=[],
    ),
    body=[
        Assign(
            targets=[Name(id="instance_serialized", ctx=Store())],
            value=Attribute(
                value=Call(
                    func=Attribute(
                        value=Name(id="self", ctx=Load()),
                        attr="__class__",
                        ctx=Load(),
                    ),
                    args=[Name(id="instance", ctx=Load())],
                    keywords=[],
                ),
                attr="data",
                ctx=Load(),
            ),
        ),
        Assign(
            targets=[Name(id="data", ctx=Store())],
            value=Call(
                func=Name(id="apply_json_patch", ctx=Load()),
                args=[],
                keywords=[
                    keyword(arg="patch", value=Name(id="data", ctx=Load())),
                    keyword(
                        arg="current_state",
                        value=Name(id="instance_serialized", ctx=Load()),
                    ),
                ],
            ),
        ),
    ],
    orelse=[],
)
