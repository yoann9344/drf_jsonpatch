from ast import (
    Assign,
    Attribute,
    BinOp,
    Call,
    ClassDef,
    Constant,
    ExceptHandler,
    Expr,
    FunctionDef,
    Import,
    Load,
    Mod,
    Name,
    Raise,
    Return,
    Store,
    Try,
    alias,
    arg,
    arguments,
)


import_jsonpatch = Import(names=[alias(name="jsonpatch")])

class_JSONPatchParser = ClassDef(
    name="JSONPatchParser",
    bases=[Name(id="JSONParser", ctx=Load())],
    keywords=[],
    body=[
        Expr(
            value=Constant(
                value="\n    Parses PATCH RFC 6902 JSON-serialized data.\n    "
            )
        ),
        Assign(
            targets=[Name(id="media_type", ctx=Store())],
            value=Constant(value="application/json-patch+json"),
        ),
        FunctionDef(
            name="parse",
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg="self"),
                    arg(arg="stream"),
                    arg(arg="media_type"),
                    arg(arg="parser_context"),
                ],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[Constant(value=None), Constant(value=None)],
            ),
            body=[
                Expr(
                    value=Constant(
                        value=(
                            "\n        Parses the incoming bytestream as JSON"
                            " and returns the resulting data as json patch.\n  "
                            "      "
                        )
                    )
                ),
                Assign(
                    targets=[Name(id="data", ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Name(id="super", ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            attr="parse",
                            ctx=Load(),
                        ),
                        args=[
                            Name(id="stream", ctx=Load()),
                            Name(id="media_type", ctx=Load()),
                            Name(id="parser_context", ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Try(
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="jsonpatch", ctx=Load()),
                                    attr="JsonPatch",
                                    ctx=Load(),
                                ),
                                args=[Name(id="data", ctx=Load())],
                                keywords=[],
                            )
                        )
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Attribute(
                                value=Name(id="jsonpatch", ctx=Load()),
                                attr="InvalidJsonPatch",
                                ctx=Load(),
                            ),
                            name="exc",
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id="ParseError", ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(
                                                    value=(
                                                        "JSON Patch (rfc 6902)"
                                                        " invalid - %s"
                                                    )
                                                ),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id="str", ctx=Load()),
                                                    args=[Name(id="exc", ctx=Load())],
                                                    keywords=[],
                                                ),
                                            )
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                        )
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            decorator_list=[],
        ),
    ],
    decorator_list=[],
)
