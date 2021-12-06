Module(
    body=[
        Expr(
            value=Constant(
                value=(
                    "\nParsers are used to parse the content of incoming HTTP"
                    " requests.\n\nThey give us a generic way of being able to handle"
                    " various media types\non the request, such as form content or json"
                    " encoded data.\n"
                )
            )
        ),
        Import(names=[alias(name="codecs")]),
        ImportFrom(module="urllib", names=[alias(name="parse")], level=0),
        ImportFrom(module="django.conf", names=[alias(name="settings")], level=0),
        ImportFrom(
            module="django.core.files.uploadhandler",
            names=[alias(name="StopFutureHandlers")],
            level=0,
        ),
        ImportFrom(module="django.http", names=[alias(name="QueryDict")], level=0),
        ImportFrom(
            module="django.http.multipartparser",
            names=[alias(name="ChunkIter")],
            level=0,
        ),
        ImportFrom(
            module="django.http.multipartparser",
            names=[alias(name="MultiPartParser", asname="DjangoMultiPartParser")],
            level=0,
        ),
        ImportFrom(
            module="django.http.multipartparser",
            names=[alias(name="MultiPartParserError"), alias(name="parse_header")],
            level=0,
        ),
        ImportFrom(
            module="django.utils.encoding", names=[alias(name="force_str")], level=0
        ),
        ImportFrom(module="rest_framework", names=[alias(name="renderers")], level=0),
        ImportFrom(
            module="rest_framework.exceptions",
            names=[alias(name="ParseError")],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.settings",
            names=[alias(name="api_settings")],
            level=0,
        ),
        ImportFrom(module="rest_framework.utils", names=[alias(name="json")], level=0),
        ClassDef(
            name="DataAndFiles",
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name="__init__",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="data"), arg(arg="files")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="data",
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id="data", ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="files",
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id="files", ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                )
            ],
            decorator_list=[],
        ),
        ClassDef(
            name="BaseParser",
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(
                        value=(
                            "\n    All parsers should extend `BaseParser`, specifying a"
                            " `media_type`\n    attribute, and overriding the"
                            " `.parse()` method.\n    "
                        )
                    )
                ),
                Assign(
                    targets=[Name(id="media_type", ctx=Store())],
                    value=Constant(value=None),
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
                                    "\n        Given a stream to read from, return the"
                                    " parsed representation.\n        Should return"
                                    " parsed data, or a `DataAndFiles` object"
                                    " consisting of the\n        parsed data and"
                                    " files.\n        "
                                )
                            )
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id="NotImplementedError", ctx=Load()),
                                args=[Constant(value=".parse() must be overridden.")],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name="JSONParser",
            bases=[Name(id="BaseParser", ctx=Load())],
            keywords=[],
            body=[
                Expr(value=Constant(value="\n    Parses JSON-serialized data.\n    ")),
                Assign(
                    targets=[Name(id="media_type", ctx=Store())],
                    value=Constant(value="application/json"),
                ),
                Assign(
                    targets=[Name(id="renderer_class", ctx=Store())],
                    value=Attribute(
                        value=Name(id="renderers", ctx=Load()),
                        attr="JSONRenderer",
                        ctx=Load(),
                    ),
                ),
                Assign(
                    targets=[Name(id="strict", ctx=Store())],
                    value=Attribute(
                        value=Name(id="api_settings", ctx=Load()),
                        attr="STRICT_JSON",
                        ctx=Load(),
                    ),
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
                                    " and returns the resulting data.\n        "
                                )
                            )
                        ),
                        Assign(
                            targets=[Name(id="parser_context", ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id="parser_context", ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="encoding", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="parser_context", ctx=Load()),
                                    attr="get",
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="encoding"),
                                    Attribute(
                                        value=Name(id="settings", ctx=Load()),
                                        attr="DEFAULT_CHARSET",
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id="decoded_stream", ctx=Store())],
                                    value=Call(
                                        func=Call(
                                            func=Attribute(
                                                value=Name(id="codecs", ctx=Load()),
                                                attr="getreader",
                                                ctx=Load(),
                                            ),
                                            args=[Name(id="encoding", ctx=Load())],
                                            keywords=[],
                                        ),
                                        args=[Name(id="stream", ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id="parse_constant", ctx=Store())],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="strict",
                                            ctx=Load(),
                                        ),
                                        body=Attribute(
                                            value=Name(id="json", ctx=Load()),
                                            attr="strict_constant",
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=None),
                                    ),
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="json", ctx=Load()),
                                            attr="load",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="decoded_stream", ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg="parse_constant",
                                                value=Name(
                                                    id="parse_constant", ctx=Load()
                                                ),
                                            )
                                        ],
                                    )
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id="ValueError", ctx=Load()),
                                    name="exc",
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id="ParseError", ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(
                                                            value=(
                                                                "JSON parse error - %s"
                                                            )
                                                        ),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Name(
                                                                id="str", ctx=Load()
                                                            ),
                                                            args=[
                                                                Name(
                                                                    id="exc", ctx=Load()
                                                                )
                                                            ],
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
        ),
        ClassDef(
            name="FormParser",
            bases=[Name(id="BaseParser", ctx=Load())],
            keywords=[],
            body=[
                Expr(value=Constant(value="\n    Parser for form data.\n    ")),
                Assign(
                    targets=[Name(id="media_type", ctx=Store())],
                    value=Constant(value="application/x-www-form-urlencoded"),
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
                                    "\n        Parses the incoming bytestream as a URL"
                                    " encoded form,\n        and returns the resulting"
                                    " QueryDict.\n        "
                                )
                            )
                        ),
                        Assign(
                            targets=[Name(id="parser_context", ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id="parser_context", ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="encoding", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="parser_context", ctx=Load()),
                                    attr="get",
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="encoding"),
                                    Attribute(
                                        value=Name(id="settings", ctx=Load()),
                                        attr="DEFAULT_CHARSET",
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id="QueryDict", ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id="stream", ctx=Load()),
                                            attr="read",
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    )
                                ],
                                keywords=[
                                    keyword(
                                        arg="encoding",
                                        value=Name(id="encoding", ctx=Load()),
                                    )
                                ],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name="MultiPartParser",
            bases=[Name(id="BaseParser", ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(
                        value=(
                            "\n    Parser for multipart form data, which may include"
                            " file data.\n    "
                        )
                    )
                ),
                Assign(
                    targets=[Name(id="media_type", ctx=Store())],
                    value=Constant(value="multipart/form-data"),
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
                                    "\n        Parses the incoming bytestream as a"
                                    " multipart encoded form,\n        and returns a"
                                    " DataAndFiles object.\n\n        `.data` will be a"
                                    " `QueryDict` containing all the form parameters.\n"
                                    "        `.files` will be a `QueryDict` containing"
                                    " all the form files.\n        "
                                )
                            )
                        ),
                        Assign(
                            targets=[Name(id="parser_context", ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id="parser_context", ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="request", ctx=Store())],
                            value=Subscript(
                                value=Name(id="parser_context", ctx=Load()),
                                slice=Constant(value="request"),
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id="encoding", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="parser_context", ctx=Load()),
                                    attr="get",
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="encoding"),
                                    Attribute(
                                        value=Name(id="settings", ctx=Load()),
                                        attr="DEFAULT_CHARSET",
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="meta", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id="request", ctx=Load()),
                                        attr="META",
                                        ctx=Load(),
                                    ),
                                    attr="copy",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id="meta", ctx=Load()),
                                    slice=Constant(value="CONTENT_TYPE"),
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id="media_type", ctx=Load()),
                        ),
                        Assign(
                            targets=[Name(id="upload_handlers", ctx=Store())],
                            value=Attribute(
                                value=Name(id="request", ctx=Load()),
                                attr="upload_handlers",
                                ctx=Load(),
                            ),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id="parser", ctx=Store())],
                                    value=Call(
                                        func=Name(
                                            id="DjangoMultiPartParser", ctx=Load()
                                        ),
                                        args=[
                                            Name(id="meta", ctx=Load()),
                                            Name(id="stream", ctx=Load()),
                                            Name(id="upload_handlers", ctx=Load()),
                                            Name(id="encoding", ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id="data", ctx=Store()),
                                                Name(id="files", ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="parser", ctx=Load()),
                                            attr="parse",
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id="DataAndFiles", ctx=Load()),
                                        args=[
                                            Name(id="data", ctx=Load()),
                                            Name(id="files", ctx=Load()),
                                        ],
                                        keywords=[],
                                    )
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id="MultiPartParserError", ctx=Load()),
                                    name="exc",
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id="ParseError", ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(
                                                            value=(
                                                                "Multipart form parse"
                                                                " error - %s"
                                                            )
                                                        ),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Name(
                                                                id="str", ctx=Load()
                                                            ),
                                                            args=[
                                                                Name(
                                                                    id="exc", ctx=Load()
                                                                )
                                                            ],
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
        ),
        ClassDef(
            name="FileUploadParser",
            bases=[Name(id="BaseParser", ctx=Load())],
            keywords=[],
            body=[
                Expr(value=Constant(value="\n    Parser for file upload data.\n    ")),
                Assign(
                    targets=[Name(id="media_type", ctx=Store())],
                    value=Constant(value="*/*"),
                ),
                Assign(
                    targets=[Name(id="errors", ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value="unhandled"),
                            Constant(value="no_filename"),
                        ],
                        values=[
                            Constant(
                                value=(
                                    "FileUpload parse error - none of upload handlers"
                                    " can handle the stream"
                                )
                            ),
                            Constant(
                                value=(
                                    "Missing filename. Request should include a"
                                    " Content-Disposition header with a filename"
                                    " parameter."
                                )
                            ),
                        ],
                    ),
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
                                    "\n        Treats the incoming bytestream as a raw"
                                    " file upload and returns\n        a `DataAndFiles`"
                                    " object.\n\n        `.data` will be None (we"
                                    " expect request body to be a file content).\n     "
                                    "   `.files` will be a `QueryDict` containing one"
                                    " 'file' element.\n        "
                                )
                            )
                        ),
                        Assign(
                            targets=[Name(id="parser_context", ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id="parser_context", ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="request", ctx=Store())],
                            value=Subscript(
                                value=Name(id="parser_context", ctx=Load()),
                                slice=Constant(value="request"),
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id="encoding", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="parser_context", ctx=Load()),
                                    attr="get",
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="encoding"),
                                    Attribute(
                                        value=Name(id="settings", ctx=Load()),
                                        attr="DEFAULT_CHARSET",
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="meta", ctx=Store())],
                            value=Attribute(
                                value=Name(id="request", ctx=Load()),
                                attr="META",
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id="upload_handlers", ctx=Store())],
                            value=Attribute(
                                value=Name(id="request", ctx=Load()),
                                attr="upload_handlers",
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id="filename", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="get_filename",
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
                        If(
                            test=UnaryOp(
                                op=Not(), operand=Name(id="filename", ctx=Load())
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id="ParseError", ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="errors",
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value="no_filename"),
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="content_type", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="meta", ctx=Load()),
                                    attr="get",
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="HTTP_CONTENT_TYPE"),
                                    Call(
                                        func=Attribute(
                                            value=Name(id="meta", ctx=Load()),
                                            attr="get",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="CONTENT_TYPE"),
                                            Constant(value=""),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id="content_length", ctx=Store())],
                                    value=Call(
                                        func=Name(id="int", ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id="meta", ctx=Load()),
                                                    attr="get",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(
                                                        value="HTTP_CONTENT_LENGTH"
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(
                                                                id="meta", ctx=Load()
                                                            ),
                                                            attr="get",
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(
                                                                value="CONTENT_LENGTH"
                                                            ),
                                                            Constant(value=0),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            )
                                        ],
                                        keywords=[],
                                    ),
                                )
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id="ValueError", ctx=Load()),
                                            Name(id="TypeError", ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id="content_length", ctx=Store())
                                            ],
                                            value=Constant(value=None),
                                        )
                                    ],
                                )
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        For(
                            target=Name(id="handler", ctx=Store()),
                            iter=Name(id="upload_handlers", ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id="result", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="handler", ctx=Load()),
                                            attr="handle_raw_input",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id="stream", ctx=Load()),
                                            Name(id="meta", ctx=Load()),
                                            Name(id="content_length", ctx=Load()),
                                            Constant(value=None),
                                            Name(id="encoding", ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id="result", ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(
                                                    id="DataAndFiles", ctx=Load()
                                                ),
                                                args=[
                                                    Dict(keys=[], values=[]),
                                                    Dict(
                                                        keys=[Constant(value="file")],
                                                        values=[
                                                            Subscript(
                                                                value=Name(
                                                                    id="result",
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=1),
                                                                ctx=Load(),
                                                            )
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            )
                                        )
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="possible_sizes", ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id="x", ctx=Load()),
                                    attr="chunk_size",
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id="x", ctx=Store()),
                                        iter=Name(id="upload_handlers", ctx=Load()),
                                        ifs=[
                                            Attribute(
                                                value=Name(id="x", ctx=Load()),
                                                attr="chunk_size",
                                                ctx=Load(),
                                            )
                                        ],
                                        is_async=0,
                                    )
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="chunk_size", ctx=Store())],
                            value=Call(
                                func=Name(id="min", ctx=Load()),
                                args=[
                                    BinOp(
                                        left=List(
                                            elts=[
                                                BinOp(
                                                    left=BinOp(
                                                        left=Constant(value=2),
                                                        op=Pow(),
                                                        right=Constant(value=31),
                                                    ),
                                                    op=Sub(),
                                                    right=Constant(value=4),
                                                )
                                            ],
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Name(id="possible_sizes", ctx=Load()),
                                    )
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="chunks", ctx=Store())],
                            value=Call(
                                func=Name(id="ChunkIter", ctx=Load()),
                                args=[
                                    Name(id="stream", ctx=Load()),
                                    Name(id="chunk_size", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="counters", ctx=Store())],
                            value=BinOp(
                                left=List(elts=[Constant(value=0)], ctx=Load()),
                                op=Mult(),
                                right=Call(
                                    func=Name(id="len", ctx=Load()),
                                    args=[Name(id="upload_handlers", ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id="index", ctx=Store()),
                                    Name(id="handler", ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id="enumerate", ctx=Load()),
                                args=[Name(id="upload_handlers", ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(
                                                        id="handler", ctx=Load()
                                                    ),
                                                    attr="new_file",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=None),
                                                    Name(id="filename", ctx=Load()),
                                                    Name(id="content_type", ctx=Load()),
                                                    Name(
                                                        id="content_length", ctx=Load()
                                                    ),
                                                    Name(id="encoding", ctx=Load()),
                                                ],
                                                keywords=[],
                                            )
                                        )
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(
                                                id="StopFutureHandlers", ctx=Load()
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Name(
                                                            id="upload_handlers",
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Subscript(
                                                        value=Name(
                                                            id="upload_handlers",
                                                            ctx=Load(),
                                                        ),
                                                        slice=Slice(
                                                            upper=BinOp(
                                                                left=Name(
                                                                    id="index",
                                                                    ctx=Load(),
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value=1),
                                                            )
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Break(),
                                            ],
                                        )
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                )
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id="chunk", ctx=Store()),
                            iter=Name(id="chunks", ctx=Load()),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id="index", ctx=Store()),
                                            Name(id="handler", ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id="enumerate", ctx=Load()),
                                        args=[Name(id="upload_handlers", ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id="chunk_length", ctx=Store())
                                            ],
                                            value=Call(
                                                func=Name(id="len", ctx=Load()),
                                                args=[Name(id="chunk", ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id="chunk", ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(
                                                        id="handler", ctx=Load()
                                                    ),
                                                    attr="receive_data_chunk",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id="chunk", ctx=Load()),
                                                    Subscript(
                                                        value=Name(
                                                            id="counters", ctx=Load()
                                                        ),
                                                        slice=Name(
                                                            id="index", ctx=Load()
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id="counters", ctx=Load()),
                                                slice=Name(id="index", ctx=Load()),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id="chunk_length", ctx=Load()),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id="chunk", ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None)],
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                )
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id="index", ctx=Store()),
                                    Name(id="handler", ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id="enumerate", ctx=Load()),
                                args=[Name(id="upload_handlers", ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="file_obj", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="handler", ctx=Load()),
                                            attr="file_complete",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id="counters", ctx=Load()),
                                                slice=Name(id="index", ctx=Load()),
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id="file_obj", ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(
                                                    id="DataAndFiles", ctx=Load()
                                                ),
                                                args=[
                                                    Dict(keys=[], values=[]),
                                                    Dict(
                                                        keys=[Constant(value="file")],
                                                        values=[
                                                            Name(
                                                                id="file_obj",
                                                                ctx=Load(),
                                                            )
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            )
                                        )
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id="ParseError", ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="errors",
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value="unhandled"),
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_filename",
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
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value=(
                                    "\n        Detects the uploaded file name. First"
                                    " searches a 'filename' url kwarg.\n        Then"
                                    " tries to parse Content-Disposition header.\n   "
                                    "     "
                                )
                            )
                        ),
                        Try(
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id="parser_context", ctx=Load()),
                                            slice=Constant(value="kwargs"),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value="filename"),
                                        ctx=Load(),
                                    )
                                )
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id="KeyError", ctx=Load()), body=[Pass()]
                                )
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id="meta", ctx=Store())],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Name(id="parser_context", ctx=Load()),
                                            slice=Constant(value="request"),
                                            ctx=Load(),
                                        ),
                                        attr="META",
                                        ctx=Load(),
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id="disposition", ctx=Store())],
                                    value=Call(
                                        func=Name(id="parse_header", ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(
                                                            id="meta", ctx=Load()
                                                        ),
                                                        slice=Constant(
                                                            value="HTTP_CONTENT_DISPOSITION"
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr="encode",
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            )
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id="filename_parm", ctx=Store())],
                                    value=Subscript(
                                        value=Name(id="disposition", ctx=Load()),
                                        slice=Constant(value=1),
                                        ctx=Load(),
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value="filename*"),
                                        ops=[In()],
                                        comparators=[
                                            Name(id="filename_parm", ctx=Load())
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="get_encoded_filename",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id="filename_parm", ctx=Load())
                                                ],
                                                keywords=[],
                                            )
                                        )
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id="force_str", ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(
                                                    id="filename_parm", ctx=Load()
                                                ),
                                                slice=Constant(value="filename"),
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    )
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id="AttributeError", ctx=Load()),
                                            Name(id="KeyError", ctx=Load()),
                                            Name(id="ValueError", ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[Pass()],
                                )
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_encoded_filename",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="filename_parm")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value=(
                                    "\n        Handle encoded filenames per RFC6266."
                                    " See also:\n       "
                                    " https://tools.ietf.org/html/rfc2231#section-4\n  "
                                    "      "
                                )
                            )
                        ),
                        Assign(
                            targets=[Name(id="encoded_filename", ctx=Store())],
                            value=Call(
                                func=Name(id="force_str", ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id="filename_parm", ctx=Load()),
                                        slice=Constant(value="filename*"),
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id="charset", ctx=Store()),
                                                Name(id="lang", ctx=Store()),
                                                Name(id="filename", ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(
                                                id="encoded_filename", ctx=Load()
                                            ),
                                            attr="split",
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value="'"), Constant(value=2)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id="filename", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="parse", ctx=Load()),
                                            attr="unquote",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="filename", ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id="ValueError", ctx=Load()),
                                            Name(id="LookupError", ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id="filename", ctx=Store())],
                                            value=Call(
                                                func=Name(id="force_str", ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(
                                                            id="filename_parm",
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(
                                                            value="filename"
                                                        ),
                                                        ctx=Load(),
                                                    )
                                                ],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                )
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(value=Name(id="filename", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
