

Module(
    body=[
        Expr(
            value=Constant(
                value="\nSerializers and ModelSerializers are similar to Forms and ModelForms.\nUnlike forms, they are not constrained to dealing with HTML output, and\nform encoded input.\n\nSerialization in REST framework is a two-phase process:\n\n1. Serializers marshal between complex types like model instances, and\npython primitives.\n2. The process of marshalling between python primitives and request and\nresponse content is handled by parsers and renderers.\n"
            )
        ),
        Import(names=[alias(name="copy")]),
        Import(names=[alias(name="inspect")]),
        Import(names=[alias(name="traceback")]),
        ImportFrom(
            module="collections",
            names=[alias(name="OrderedDict"), alias(name="defaultdict")],
            level=0,
        ),
        ImportFrom(module="collections.abc", names=[alias(name="Mapping")], level=0),
        ImportFrom(
            module="django.core.exceptions",
            names=[alias(name="FieldDoesNotExist"), alias(name="ImproperlyConfigured")],
            level=0,
        ),
        ImportFrom(
            module="django.core.exceptions",
            names=[alias(name="ValidationError", asname="DjangoValidationError")],
            level=0,
        ),
        ImportFrom(module="django.db", names=[alias(name="models")], level=0),
        ImportFrom(
            module="django.db.models.fields",
            names=[alias(name="Field", asname="DjangoModelField")],
            level=0,
        ),
        ImportFrom(module="django.utils", names=[alias(name="timezone")], level=0),
        ImportFrom(
            module="django.utils.functional",
            names=[alias(name="cached_property")],
            level=0,
        ),
        ImportFrom(
            module="django.utils.translation",
            names=[alias(name="gettext_lazy", asname="_")],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.compat",
            names=[alias(name="postgres_fields")],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.exceptions",
            names=[alias(name="ErrorDetail"), alias(name="ValidationError")],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.fields",
            names=[alias(name="get_error_detail"), alias(name="set_value")],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.settings",
            names=[alias(name="api_settings")],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.utils",
            names=[
                alias(name="html"),
                alias(name="model_meta"),
                alias(name="representation"),
            ],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.utils.field_mapping",
            names=[
                alias(name="ClassLookupDict"),
                alias(name="get_field_kwargs"),
                alias(name="get_nested_relation_kwargs"),
                alias(name="get_relation_kwargs"),
                alias(name="get_url_kwargs"),
            ],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.utils.serializer_helpers",
            names=[
                alias(name="BindingDict"),
                alias(name="BoundField"),
                alias(name="JSONBoundField"),
                alias(name="NestedBoundField"),
                alias(name="ReturnDict"),
                alias(name="ReturnList"),
            ],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.validators",
            names=[
                alias(name="UniqueForDateValidator"),
                alias(name="UniqueForMonthValidator"),
                alias(name="UniqueForYearValidator"),
                alias(name="UniqueTogetherValidator"),
            ],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.fields",
            names=[
                alias(name="BooleanField"),
                alias(name="CharField"),
                alias(name="ChoiceField"),
                alias(name="DateField"),
                alias(name="DateTimeField"),
                alias(name="DecimalField"),
                alias(name="DictField"),
                alias(name="DurationField"),
                alias(name="EmailField"),
                alias(name="Field"),
                alias(name="FileField"),
                alias(name="FilePathField"),
                alias(name="FloatField"),
                alias(name="HiddenField"),
                alias(name="HStoreField"),
                alias(name="IPAddressField"),
                alias(name="ImageField"),
                alias(name="IntegerField"),
                alias(name="JSONField"),
                alias(name="ListField"),
                alias(name="ModelField"),
                alias(name="MultipleChoiceField"),
                alias(name="NullBooleanField"),
                alias(name="ReadOnlyField"),
                alias(name="RegexField"),
                alias(name="SerializerMethodField"),
                alias(name="SlugField"),
                alias(name="TimeField"),
                alias(name="URLField"),
                alias(name="UUIDField"),
            ],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.relations",
            names=[
                alias(name="HyperlinkedIdentityField"),
                alias(name="HyperlinkedRelatedField"),
                alias(name="ManyRelatedField"),
                alias(name="PrimaryKeyRelatedField"),
                alias(name="RelatedField"),
                alias(name="SlugRelatedField"),
                alias(name="StringRelatedField"),
            ],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.fields",
            names=[
                alias(name="CreateOnlyDefault"),
                alias(name="CurrentUserDefault"),
                alias(name="SkipField"),
                alias(name="empty"),
            ],
            level=0,
        ),
        ImportFrom(
            module="rest_framework.relations",
            names=[alias(name="Hyperlink"), alias(name="PKOnlyObject")],
            level=0,
        ),
        Assign(
            targets=[Name(id="LIST_SERIALIZER_KWARGS", ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value="read_only"),
                    Constant(value="write_only"),
                    Constant(value="required"),
                    Constant(value="default"),
                    Constant(value="initial"),
                    Constant(value="source"),
                    Constant(value="label"),
                    Constant(value="help_text"),
                    Constant(value="style"),
                    Constant(value="error_messages"),
                    Constant(value="allow_empty"),
                    Constant(value="instance"),
                    Constant(value="data"),
                    Constant(value="partial"),
                    Constant(value="context"),
                    Constant(value="allow_null"),
                ],
                ctx=Load(),
            ),
        ),
        Assign(
            targets=[Name(id="ALL_FIELDS", ctx=Store())],
            value=Constant(value="__all__"),
        ),
        ClassDef(
            name="BaseSerializer",
            bases=[Name(id="Field", ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(
                        value="\n    The BaseSerializer class provides a minimal class which may be used\n    for writing custom serializer implementations.\n\n    Note that we strongly restrict the ordering of operations/properties\n    that may be used on the serializer in order to enforce correct usage.\n\n    In particular, if a `data=` argument is passed then:\n\n    .is_valid() - Available.\n    .initial_data - Available.\n    .validated_data - Only available after calling `is_valid()`\n    .errors - Only available after calling `is_valid()`\n    .data - Only available after calling `is_valid()`\n\n    If a `data=` argument is not passed then:\n\n    .is_valid() - Not available.\n    .initial_data - Not available.\n    .validated_data - Not available.\n    .errors - Not available.\n    .data - Available.\n    "
                    )
                ),
                FunctionDef(
                    name="__init__",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="instance"), arg(arg="data")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg="kwargs"),
                        defaults=[Constant(value=None), Name(id="empty", ctx=Load())],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="instance",
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id="instance", ctx=Load()),
                        ),
                        If(
                            test=Compare(
                                left=Name(id="data", ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Name(id="empty", ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="initial_data",
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Name(id="data", ctx=Load()),
                                )
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="partial",
                                    ctx=Store(),
                                )
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="kwargs", ctx=Load()),
                                    attr="pop",
                                    ctx=Load(),
                                ),
                                args=[Constant(value="partial"), Constant(value=False)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="_context",
                                    ctx=Store(),
                                )
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="kwargs", ctx=Load()),
                                    attr="pop",
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="context"),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="kwargs", ctx=Load()),
                                    attr="pop",
                                    ctx=Load(),
                                ),
                                args=[Constant(value="many"), Constant(value=None)],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id="super", ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr="__init__",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[keyword(value=Name(id="kwargs", ctx=Load()))],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="__new__",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="cls")],
                        vararg=arg(arg="args"),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg="kwargs"),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id="kwargs", ctx=Load()),
                                    attr="pop",
                                    ctx=Load(),
                                ),
                                args=[Constant(value="many"), Constant(value=False)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="cls", ctx=Load()),
                                            attr="many_init",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Name(id="args", ctx=Load()),
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[
                                            keyword(value=Name(id="kwargs", ctx=Load()))
                                        ],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id="super", ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr="__new__",
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id="cls", ctx=Load()),
                                    Starred(
                                        value=Name(id="args", ctx=Load()), ctx=Load()
                                    ),
                                ],
                                keywords=[keyword(value=Name(id="kwargs", ctx=Load()))],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="__class_getitem__",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="cls")],
                        vararg=arg(arg="args"),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg="kwargs"),
                        defaults=[],
                    ),
                    body=[Return(value=Name(id="cls", ctx=Load()))],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="many_init",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="cls")],
                        vararg=arg(arg="args"),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg="kwargs"),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        This method implements the creation of a `ListSerializer` parent\n        class when `many=True` is used. You can customize it if you need to\n        control which keyword arguments are passed to the parent, and\n        which are passed to the child.\n\n        Note that we're over-cautious in passing most arguments to both parent\n        and child classes in order to try to cover the general case. If you're\n        overriding this method you'll probably want something much simpler, eg:\n\n        @classmethod\n        def many_init(cls, *args, **kwargs):\n            kwargs['child'] = cls()\n            return CustomListSerializer(*args, **kwargs)\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="allow_empty", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="kwargs", ctx=Load()),
                                    attr="pop",
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="allow_empty"),
                                    Constant(value=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="child_serializer", ctx=Store())],
                            value=Call(
                                func=Name(id="cls", ctx=Load()),
                                args=[
                                    Starred(
                                        value=Name(id="args", ctx=Load()), ctx=Load()
                                    )
                                ],
                                keywords=[keyword(value=Name(id="kwargs", ctx=Load()))],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="list_kwargs", ctx=Store())],
                            value=Dict(
                                keys=[Constant(value="child")],
                                values=[Name(id="child_serializer", ctx=Load())],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id="allow_empty", ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id="list_kwargs", ctx=Load()),
                                            slice=Constant(value="allow_empty"),
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Name(id="allow_empty", ctx=Load()),
                                )
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="list_kwargs", ctx=Load()),
                                    attr="update",
                                    ctx=Load(),
                                ),
                                args=[
                                    DictComp(
                                        key=Name(id="key", ctx=Load()),
                                        value=Name(id="value", ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id="key", ctx=Store()),
                                                        Name(id="value", ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(
                                                            id="kwargs", ctx=Load()
                                                        ),
                                                        attr="items",
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id="key", ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Name(
                                                                id="LIST_SERIALIZER_KWARGS",
                                                                ctx=Load(),
                                                            )
                                                        ],
                                                    )
                                                ],
                                                is_async=0,
                                            )
                                        ],
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Assign(
                            targets=[Name(id="meta", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Name(id="cls", ctx=Load()),
                                    Constant(value="Meta"),
                                    Constant(value=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="list_serializer_class", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Name(id="meta", ctx=Load()),
                                    Constant(value="list_serializer_class"),
                                    Name(id="ListSerializer", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id="list_serializer_class", ctx=Load()),
                                args=[
                                    Starred(
                                        value=Name(id="args", ctx=Load()), ctx=Load()
                                    )
                                ],
                                keywords=[
                                    keyword(value=Name(id="list_kwargs", ctx=Load()))
                                ],
                            )
                        ),
                    ],
                    decorator_list=[Name(id="classmethod", ctx=Load())],
                ),
                FunctionDef(
                    name="to_internal_value",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="data")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id="NotImplementedError", ctx=Load()),
                                args=[
                                    Constant(
                                        value="`to_internal_value()` must be implemented."
                                    )
                                ],
                                keywords=[],
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="to_representation",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="instance")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id="NotImplementedError", ctx=Load()),
                                args=[
                                    Constant(
                                        value="`to_representation()` must be implemented."
                                    )
                                ],
                                keywords=[],
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="update",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="instance"),
                            arg(arg="validated_data"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id="NotImplementedError", ctx=Load()),
                                args=[
                                    Constant(value="`update()` must be implemented.")
                                ],
                                keywords=[],
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="create",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="validated_data")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id="NotImplementedError", ctx=Load()),
                                args=[
                                    Constant(value="`create()` must be implemented.")
                                ],
                                keywords=[],
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="save",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg="kwargs"),
                        defaults=[],
                    ),
                    body=[
                        Assert(
                            test=Call(
                                func=Name(id="hasattr", ctx=Load()),
                                args=[
                                    Name(id="self", ctx=Load()),
                                    Constant(value="_errors"),
                                ],
                                keywords=[],
                            ),
                            msg=Constant(
                                value="You must call `.is_valid()` before calling `.save()`."
                            ),
                        ),
                        Assert(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="errors",
                                    ctx=Load(),
                                ),
                            ),
                            msg=Constant(
                                value="You cannot call `.save()` on a serializer with invalid data."
                            ),
                        ),
                        Assert(
                            test=Compare(
                                left=Constant(value="commit"),
                                ops=[NotIn()],
                                comparators=[Name(id="kwargs", ctx=Load())],
                            ),
                            msg=Constant(
                                value="'commit' is not a valid keyword argument to the 'save()' method. If you need to access data before committing to the database then inspect 'serializer.validated_data' instead. You can also pass additional keyword arguments to 'save()' if you need to set extra attributes on the saved model instance. For example: 'serializer.save(owner=request.user)'.'"
                            ),
                        ),
                        Assert(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="hasattr", ctx=Load()),
                                    args=[
                                        Name(id="self", ctx=Load()),
                                        Constant(value="_data"),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            msg=Constant(
                                value="You cannot call `.save()` after accessing `serializer.data`.If you need to access data before committing to the database then inspect 'serializer.validated_data' instead. "
                            ),
                        ),
                        Assign(
                            targets=[Name(id="validated_data", ctx=Store())],
                            value=Dict(
                                keys=[None, None],
                                values=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="validated_data",
                                        ctx=Load(),
                                    ),
                                    Name(id="kwargs", ctx=Load()),
                                ],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="instance",
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="instance",
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="update",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id="self", ctx=Load()),
                                                attr="instance",
                                                ctx=Load(),
                                            ),
                                            Name(id="validated_data", ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assert(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="instance",
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None)],
                                    ),
                                    msg=Constant(
                                        value="`update()` did not return an object instance."
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="instance",
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="create",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="validated_data", ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assert(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="instance",
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None)],
                                    ),
                                    msg=Constant(
                                        value="`create()` did not return an object instance."
                                    ),
                                ),
                            ],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id="self", ctx=Load()),
                                attr="instance",
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="is_valid",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="raise_exception")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[Constant(value=False)],
                    ),
                    body=[
                        Assert(
                            test=Call(
                                func=Name(id="hasattr", ctx=Load()),
                                args=[
                                    Name(id="self", ctx=Load()),
                                    Constant(value="initial_data"),
                                ],
                                keywords=[],
                            ),
                            msg=Constant(
                                value="Cannot call `.is_valid()` as no `data=` keyword argument was passed when instantiating the serializer instance."
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="hasattr", ctx=Load()),
                                    args=[
                                        Name(id="self", ctx=Load()),
                                        Constant(value="_validated_data"),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="_validated_data",
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="run_validation",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(
                                                            id="self", ctx=Load()
                                                        ),
                                                        attr="initial_data",
                                                        ctx=Load(),
                                                    )
                                                ],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id="ValidationError", ctx=Load()),
                                            name="exc",
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="_validated_data",
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Dict(keys=[], values=[]),
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="_errors",
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Attribute(
                                                        value=Name(
                                                            id="exc", ctx=Load()
                                                        ),
                                                        attr="detail",
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        )
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="_errors",
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=Dict(keys=[], values=[]),
                                        )
                                    ],
                                    finalbody=[],
                                )
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="_errors",
                                        ctx=Load(),
                                    ),
                                    Name(id="raise_exception", ctx=Load()),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id="ValidationError", ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id="self", ctx=Load()),
                                                attr="errors",
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="bool", ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="_errors",
                                            ctx=Load(),
                                        )
                                    ],
                                    keywords=[],
                                ),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="data",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id="hasattr", ctx=Load()),
                                        args=[
                                            Name(id="self", ctx=Load()),
                                            Constant(value="initial_data"),
                                        ],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id="hasattr", ctx=Load()),
                                            args=[
                                                Name(id="self", ctx=Load()),
                                                Constant(value="_validated_data"),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="msg", ctx=Store())],
                                    value=Constant(
                                        value="When a serializer is passed a `data` keyword argument you must call `.is_valid()` before attempting to access the serialized `.data` representation.\nYou should either call `.is_valid()` first, or access `.initial_data` instead."
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id="AssertionError", ctx=Load()),
                                        args=[Name(id="msg", ctx=Load())],
                                        keywords=[],
                                    )
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="hasattr", ctx=Load()),
                                    args=[
                                        Name(id="self", ctx=Load()),
                                        Constant(value="_data"),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="instance",
                                                    ctx=Load(),
                                                ),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None)],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id="getattr", ctx=Load()),
                                                    args=[
                                                        Name(id="self", ctx=Load()),
                                                        Constant(value="_errors"),
                                                        Constant(value=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="_data",
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="to_representation",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(
                                                            id="self", ctx=Load()
                                                        ),
                                                        attr="instance",
                                                        ctx=Load(),
                                                    )
                                                ],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Name(
                                                            id="hasattr", ctx=Load()
                                                        ),
                                                        args=[
                                                            Name(id="self", ctx=Load()),
                                                            Constant(
                                                                value="_validated_data"
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(
                                                                id="getattr", ctx=Load()
                                                            ),
                                                            args=[
                                                                Name(
                                                                    id="self",
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(
                                                                    value="_errors"
                                                                ),
                                                                Constant(value=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="_data",
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="to_representation",
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(
                                                                    id="self",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="validated_data",
                                                                ctx=Load(),
                                                            )
                                                        ],
                                                        keywords=[],
                                                    ),
                                                )
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="_data",
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="get_initial",
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                )
                                            ],
                                        )
                                    ],
                                )
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id="self", ctx=Load()),
                                attr="_data",
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[Name(id="property", ctx=Load())],
                ),
                FunctionDef(
                    name="errors",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="hasattr", ctx=Load()),
                                    args=[
                                        Name(id="self", ctx=Load()),
                                        Constant(value="_errors"),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="msg", ctx=Store())],
                                    value=Constant(
                                        value="You must call `.is_valid()` before accessing `.errors`."
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id="AssertionError", ctx=Load()),
                                        args=[Name(id="msg", ctx=Load())],
                                        keywords=[],
                                    )
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id="self", ctx=Load()),
                                attr="_errors",
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[Name(id="property", ctx=Load())],
                ),
                FunctionDef(
                    name="validated_data",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="hasattr", ctx=Load()),
                                    args=[
                                        Name(id="self", ctx=Load()),
                                        Constant(value="_validated_data"),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="msg", ctx=Store())],
                                    value=Constant(
                                        value="You must call `.is_valid()` before accessing `.validated_data`."
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id="AssertionError", ctx=Load()),
                                        args=[Name(id="msg", ctx=Load())],
                                        keywords=[],
                                    )
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id="self", ctx=Load()),
                                attr="_validated_data",
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[Name(id="property", ctx=Load())],
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name="SerializerMetaclass",
            bases=[Name(id="type", ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(
                        value="\n    This metaclass sets a dictionary named `_declared_fields` on the class.\n\n    Any instances of `Field` included as attributes on either the class\n    or on any of its superclasses will be include in the\n    `_declared_fields` dictionary.\n    "
                    )
                ),
                FunctionDef(
                    name="_get_declared_fields",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="cls"), arg(arg="bases"), arg(arg="attrs")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id="fields", ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Name(id="field_name", ctx=Load()),
                                        Call(
                                            func=Attribute(
                                                value=Name(id="attrs", ctx=Load()),
                                                attr="pop",
                                                ctx=Load(),
                                            ),
                                            args=[Name(id="field_name", ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id="field_name", ctx=Store()),
                                                Name(id="obj", ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Name(id="list", ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(
                                                            id="attrs", ctx=Load()
                                                        ),
                                                        attr="items",
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Call(
                                                func=Name(id="isinstance", ctx=Load()),
                                                args=[
                                                    Name(id="obj", ctx=Load()),
                                                    Name(id="Field", ctx=Load()),
                                                ],
                                                keywords=[],
                                            )
                                        ],
                                        is_async=0,
                                    )
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="fields", ctx=Load()),
                                    attr="sort",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg="key",
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg="x")],
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                defaults=[],
                                            ),
                                            body=Attribute(
                                                value=Subscript(
                                                    value=Name(id="x", ctx=Load()),
                                                    slice=Constant(value=1),
                                                    ctx=Load(),
                                                ),
                                                attr="_creation_counter",
                                                ctx=Load(),
                                            ),
                                        ),
                                    )
                                ],
                            )
                        ),
                        Assign(
                            targets=[Name(id="known", ctx=Store())],
                            value=Call(
                                func=Name(id="set", ctx=Load()),
                                args=[Name(id="attrs", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name="visit",
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg="name")],
                                kwonlyargs=[],
                                kw_defaults=[],
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="known", ctx=Load()),
                                            attr="add",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="name", ctx=Load())],
                                        keywords=[],
                                    )
                                ),
                                Return(value=Name(id="name", ctx=Load())),
                            ],
                            decorator_list=[],
                        ),
                        Assign(
                            targets=[Name(id="base_fields", ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Call(
                                            func=Name(id="visit", ctx=Load()),
                                            args=[Name(id="name", ctx=Load())],
                                            keywords=[],
                                        ),
                                        Name(id="f", ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id="base", ctx=Store()),
                                        iter=Name(id="bases", ctx=Load()),
                                        ifs=[
                                            Call(
                                                func=Name(id="hasattr", ctx=Load()),
                                                args=[
                                                    Name(id="base", ctx=Load()),
                                                    Constant(value="_declared_fields"),
                                                ],
                                                keywords=[],
                                            )
                                        ],
                                        is_async=0,
                                    ),
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id="name", ctx=Store()),
                                                Name(id="f", ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id="base", ctx=Load()),
                                                    attr="_declared_fields",
                                                    ctx=Load(),
                                                ),
                                                attr="items",
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Compare(
                                                left=Name(id="name", ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Name(id="known", ctx=Load())
                                                ],
                                            )
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id="OrderedDict", ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id="base_fields", ctx=Load()),
                                        op=Add(),
                                        right=Name(id="fields", ctx=Load()),
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[Name(id="classmethod", ctx=Load())],
                ),
                FunctionDef(
                    name="__new__",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="cls"),
                            arg(arg="name"),
                            arg(arg="bases"),
                            arg(arg="attrs"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id="attrs", ctx=Load()),
                                    slice=Constant(value="_declared_fields"),
                                    ctx=Store(),
                                )
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="cls", ctx=Load()),
                                    attr="_get_declared_fields",
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id="bases", ctx=Load()),
                                    Name(id="attrs", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id="super", ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr="__new__",
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id="cls", ctx=Load()),
                                    Name(id="name", ctx=Load()),
                                    Name(id="bases", ctx=Load()),
                                    Name(id="attrs", ctx=Load()),
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name="as_serializer_error",
            args=arguments(
                posonlyargs=[],
                args=[arg(arg="exc")],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[],
            ),
            body=[
                Assert(
                    test=Call(
                        func=Name(id="isinstance", ctx=Load()),
                        args=[
                            Name(id="exc", ctx=Load()),
                            Tuple(
                                elts=[
                                    Name(id="ValidationError", ctx=Load()),
                                    Name(id="DjangoValidationError", ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    )
                ),
                If(
                    test=Call(
                        func=Name(id="isinstance", ctx=Load()),
                        args=[
                            Name(id="exc", ctx=Load()),
                            Name(id="DjangoValidationError", ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id="detail", ctx=Store())],
                            value=Call(
                                func=Name(id="get_error_detail", ctx=Load()),
                                args=[Name(id="exc", ctx=Load())],
                                keywords=[],
                            ),
                        )
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id="detail", ctx=Store())],
                            value=Attribute(
                                value=Name(id="exc", ctx=Load()),
                                attr="detail",
                                ctx=Load(),
                            ),
                        )
                    ],
                ),
                If(
                    test=Call(
                        func=Name(id="isinstance", ctx=Load()),
                        args=[
                            Name(id="detail", ctx=Load()),
                            Name(id="Mapping", ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=DictComp(
                                key=Name(id="key", ctx=Load()),
                                value=IfExp(
                                    test=Call(
                                        func=Name(id="isinstance", ctx=Load()),
                                        args=[
                                            Name(id="value", ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Name(id="list", ctx=Load()),
                                                    Name(id="Mapping", ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=Name(id="value", ctx=Load()),
                                    orelse=List(
                                        elts=[Name(id="value", ctx=Load())], ctx=Load()
                                    ),
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id="key", ctx=Store()),
                                                Name(id="value", ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id="detail", ctx=Load()),
                                                attr="items",
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    )
                                ],
                            )
                        )
                    ],
                    orelse=[
                        If(
                            test=Call(
                                func=Name(id="isinstance", ctx=Load()),
                                args=[
                                    Name(id="detail", ctx=Load()),
                                    Name(id="list", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(
                                                    id="api_settings", ctx=Load()
                                                ),
                                                attr="NON_FIELD_ERRORS_KEY",
                                                ctx=Load(),
                                            )
                                        ],
                                        values=[Name(id="detail", ctx=Load())],
                                    )
                                )
                            ],
                            orelse=[],
                        )
                    ],
                ),
                Return(
                    value=Dict(
                        keys=[
                            Attribute(
                                value=Name(id="api_settings", ctx=Load()),
                                attr="NON_FIELD_ERRORS_KEY",
                                ctx=Load(),
                            )
                        ],
                        values=[List(elts=[Name(id="detail", ctx=Load())], ctx=Load())],
                    )
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name="Serializer",
            bases=[Name(id="BaseSerializer", ctx=Load())],
            keywords=[
                keyword(
                    arg="metaclass", value=Name(id="SerializerMetaclass", ctx=Load())
                )
            ],
            body=[
                Assign(
                    targets=[Name(id="default_error_messages", ctx=Store())],
                    value=Dict(
                        keys=[Constant(value="invalid")],
                        values=[
                            Call(
                                func=Name(id="_", ctx=Load()),
                                args=[
                                    Constant(
                                        value="Invalid data. Expected a dictionary, but got {datatype}."
                                    )
                                ],
                                keywords=[],
                            )
                        ],
                    ),
                ),
                FunctionDef(
                    name="fields",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        A dictionary of {field_name: field_instance}.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="fields", ctx=Store())],
                            value=Call(
                                func=Name(id="BindingDict", ctx=Load()),
                                args=[Name(id="self", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id="key", ctx=Store()),
                                    Name(id="value", ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="get_fields",
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr="items",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id="fields", ctx=Load()),
                                            slice=Name(id="key", ctx=Load()),
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Name(id="value", ctx=Load()),
                                )
                            ],
                            orelse=[],
                        ),
                        Return(value=Name(id="fields", ctx=Load())),
                    ],
                    decorator_list=[Name(id="cached_property", ctx=Load())],
                ),
                FunctionDef(
                    name="_writable_fields",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id="field", ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="fields",
                                        ctx=Load(),
                                    ),
                                    attr="values",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id="field", ctx=Load()),
                                            attr="read_only",
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Name(id="field", ctx=Load())
                                            )
                                        )
                                    ],
                                    orelse=[],
                                )
                            ],
                            orelse=[],
                        )
                    ],
                    decorator_list=[Name(id="property", ctx=Load())],
                ),
                FunctionDef(
                    name="_readable_fields",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id="field", ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="fields",
                                        ctx=Load(),
                                    ),
                                    attr="values",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id="field", ctx=Load()),
                                            attr="write_only",
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Name(id="field", ctx=Load())
                                            )
                                        )
                                    ],
                                    orelse=[],
                                )
                            ],
                            orelse=[],
                        )
                    ],
                    decorator_list=[Name(id="property", ctx=Load())],
                ),
                FunctionDef(
                    name="get_fields",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Returns a dictionary of {field_name: field_instance}.\n        "
                            )
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="copy", ctx=Load()),
                                    attr="deepcopy",
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="_declared_fields",
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
                    name="get_validators",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Returns a list of validator callables.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="meta", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Name(id="self", ctx=Load()),
                                    Constant(value="Meta"),
                                    Constant(value=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="validators", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Name(id="meta", ctx=Load()),
                                    Constant(value="validators"),
                                    Constant(value=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=IfExp(
                                test=Name(id="validators", ctx=Load()),
                                body=Call(
                                    func=Name(id="list", ctx=Load()),
                                    args=[Name(id="validators", ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=List(elts=[], ctx=Load()),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_initial",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id="hasattr", ctx=Load()),
                                args=[
                                    Name(id="self", ctx=Load()),
                                    Constant(value="initial_data"),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id="isinstance", ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="initial_data",
                                                    ctx=Load(),
                                                ),
                                                Name(id="Mapping", ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id="OrderedDict", ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            )
                                        )
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id="OrderedDict", ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Name(
                                                            id="field_name", ctx=Load()
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(
                                                                    id="field",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="get_value",
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(
                                                                        id="self",
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr="initial_data",
                                                                    ctx=Load(),
                                                                )
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(
                                                                    id="field_name",
                                                                    ctx=Store(),
                                                                ),
                                                                Name(
                                                                    id="field",
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(
                                                                        id="self",
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr="fields",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="items",
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(
                                                                                    id="field",
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr="get_value",
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(
                                                                                        id="self",
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr="initial_data",
                                                                                    ctx=Load(),
                                                                                )
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        ops=[IsNot()],
                                                                        comparators=[
                                                                            Name(
                                                                                id="empty",
                                                                                ctx=Load(),
                                                                            )
                                                                        ],
                                                                    ),
                                                                    UnaryOp(
                                                                        op=Not(),
                                                                        operand=Attribute(
                                                                            value=Name(
                                                                                id="field",
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr="read_only",
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            )
                                                        ],
                                                        is_async=0,
                                                    )
                                                ],
                                            )
                                        ],
                                        keywords=[],
                                    )
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id="OrderedDict", ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id="field", ctx=Load()),
                                                    attr="field_name",
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(
                                                            id="field", ctx=Load()
                                                        ),
                                                        attr="get_initial",
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id="field", ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="fields",
                                                            ctx=Load(),
                                                        ),
                                                        attr="values",
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(
                                                                id="field", ctx=Load()
                                                            ),
                                                            attr="read_only",
                                                            ctx=Load(),
                                                        ),
                                                    )
                                                ],
                                                is_async=0,
                                            )
                                        ],
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_value",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="dictionary")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id="html", ctx=Load()),
                                    attr="is_html_input",
                                    ctx=Load(),
                                ),
                                args=[Name(id="dictionary", ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id="html", ctx=Load()),
                                                    attr="parse_html_dict",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id="dictionary", ctx=Load())
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg="prefix",
                                                        value=Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="field_name",
                                                            ctx=Load(),
                                                        ),
                                                    )
                                                ],
                                            ),
                                            Name(id="empty", ctx=Load()),
                                        ],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="dictionary", ctx=Load()),
                                    attr="get",
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="field_name",
                                        ctx=Load(),
                                    ),
                                    Name(id="empty", ctx=Load()),
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="run_validation",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="data")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[Name(id="empty", ctx=Load())],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        We override the default `run_validation`, because the validation\n        performed by validators and the `.validate()` method should\n        be coerced into an error dictionary with a 'non_fields_error' key.\n        "
                            )
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id="is_empty_value", ctx=Store()),
                                        Name(id="data", ctx=Store()),
                                    ],
                                    ctx=Store(),
                                )
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="validate_empty_values",
                                    ctx=Load(),
                                ),
                                args=[Name(id="data", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id="is_empty_value", ctx=Load()),
                            body=[Return(value=Name(id="data", ctx=Load()))],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="value", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="to_internal_value",
                                    ctx=Load(),
                                ),
                                args=[Name(id="data", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="run_validators",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="value", ctx=Load())],
                                        keywords=[],
                                    )
                                ),
                                Assign(
                                    targets=[Name(id="value", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="validate",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="value", ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assert(
                                    test=Compare(
                                        left=Name(id="value", ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None)],
                                    ),
                                    msg=Constant(
                                        value=".validate() should return the validated data"
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id="ValidationError", ctx=Load()),
                                            Name(
                                                id="DjangoValidationError", ctx=Load()
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name="exc",
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(
                                                    id="ValidationError", ctx=Load()
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg="detail",
                                                        value=Call(
                                                            func=Name(
                                                                id="as_serializer_error",
                                                                ctx=Load(),
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
                                            )
                                        )
                                    ],
                                )
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(value=Name(id="value", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="_read_only_defaults",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id="fields", ctx=Store())],
                            value=ListComp(
                                elt=Name(id="field", ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id="field", ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="fields",
                                                    ctx=Load(),
                                                ),
                                                attr="values",
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(
                                                            id="field", ctx=Load()
                                                        ),
                                                        attr="read_only",
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(
                                                                id="field", ctx=Load()
                                                            ),
                                                            attr="default",
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Name(id="empty", ctx=Load())
                                                        ],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(
                                                                id="field", ctx=Load()
                                                            ),
                                                            attr="source",
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Constant(value="*")
                                                        ],
                                                    ),
                                                    Compare(
                                                        left=Constant(value="."),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(
                                                                    id="field",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="source",
                                                                ctx=Load(),
                                                            )
                                                        ],
                                                    ),
                                                ],
                                            )
                                        ],
                                        is_async=0,
                                    )
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="defaults", ctx=Store())],
                            value=Call(
                                func=Name(id="OrderedDict", ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id="field", ctx=Store()),
                            iter=Name(id="fields", ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id="default", ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="field", ctx=Load()),
                                                    attr="get_default",
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id="SkipField", ctx=Load()),
                                            body=[Continue()],
                                        )
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id="defaults", ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id="field", ctx=Load()),
                                                attr="source",
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Name(id="default", ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(value=Name(id="defaults", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="run_validators",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="value")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Add read_only fields with defaults to value before running validators.\n        "
                            )
                        ),
                        If(
                            test=Call(
                                func=Name(id="isinstance", ctx=Load()),
                                args=[
                                    Name(id="value", ctx=Load()),
                                    Name(id="dict", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="to_validate", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="_read_only_defaults",
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="to_validate", ctx=Load()),
                                            attr="update",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="value", ctx=Load())],
                                        keywords=[],
                                    )
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id="to_validate", ctx=Store())],
                                    value=Name(id="value", ctx=Load()),
                                )
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id="super", ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr="run_validators",
                                    ctx=Load(),
                                ),
                                args=[Name(id="to_validate", ctx=Load())],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="to_internal_value",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="data")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Dict of native values <- Dict of primitive datatypes.\n        "
                            )
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="isinstance", ctx=Load()),
                                    args=[
                                        Name(id="data", ctx=Load()),
                                        Name(id="Mapping", ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="message", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="error_messages",
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value="invalid"),
                                                ctx=Load(),
                                            ),
                                            attr="format",
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg="datatype",
                                                value=Attribute(
                                                    value=Call(
                                                        func=Name(
                                                            id="type", ctx=Load()
                                                        ),
                                                        args=[
                                                            Name(id="data", ctx=Load())
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr="__name__",
                                                    ctx=Load(),
                                                ),
                                            )
                                        ],
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id="ValidationError", ctx=Load()),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Attribute(
                                                        value=Name(
                                                            id="api_settings",
                                                            ctx=Load(),
                                                        ),
                                                        attr="NON_FIELD_ERRORS_KEY",
                                                        ctx=Load(),
                                                    )
                                                ],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Name(
                                                                id="message", ctx=Load()
                                                            )
                                                        ],
                                                        ctx=Load(),
                                                    )
                                                ],
                                            )
                                        ],
                                        keywords=[
                                            keyword(
                                                arg="code",
                                                value=Constant(value="invalid"),
                                            )
                                        ],
                                    )
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="ret", ctx=Store())],
                            value=Call(
                                func=Name(id="OrderedDict", ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="errors", ctx=Store())],
                            value=Call(
                                func=Name(id="OrderedDict", ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="fields", ctx=Store())],
                            value=Attribute(
                                value=Name(id="self", ctx=Load()),
                                attr="_writable_fields",
                                ctx=Load(),
                            ),
                        ),
                        For(
                            target=Name(id="field", ctx=Store()),
                            iter=Name(id="fields", ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id="validate_method", ctx=Store())],
                                    value=Call(
                                        func=Name(id="getattr", ctx=Load()),
                                        args=[
                                            Name(id="self", ctx=Load()),
                                            BinOp(
                                                left=Constant(value="validate_"),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id="field", ctx=Load()),
                                                    attr="field_name",
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Constant(value=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id="primitive_value", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="field", ctx=Load()),
                                            attr="get_value",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="data", ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id="validated_value", ctx=Store())
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="field", ctx=Load()),
                                                    attr="run_validation",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(
                                                        id="primitive_value", ctx=Load()
                                                    )
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(
                                                    id="validate_method", ctx=Load()
                                                ),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Name(
                                                            id="validated_value",
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Call(
                                                        func=Name(
                                                            id="validate_method",
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(
                                                                id="validated_value",
                                                                ctx=Load(),
                                                            )
                                                        ],
                                                        keywords=[],
                                                    ),
                                                )
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id="ValidationError", ctx=Load()),
                                            name="exc",
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(
                                                                id="errors", ctx=Load()
                                                            ),
                                                            slice=Attribute(
                                                                value=Name(
                                                                    id="field",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="field_name",
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Attribute(
                                                        value=Name(
                                                            id="exc", ctx=Load()
                                                        ),
                                                        attr="detail",
                                                        ctx=Load(),
                                                    ),
                                                )
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(
                                                id="DjangoValidationError", ctx=Load()
                                            ),
                                            name="exc",
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(
                                                                id="errors", ctx=Load()
                                                            ),
                                                            slice=Attribute(
                                                                value=Name(
                                                                    id="field",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="field_name",
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Call(
                                                        func=Name(
                                                            id="get_error_detail",
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id="exc", ctx=Load())
                                                        ],
                                                        keywords=[],
                                                    ),
                                                )
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id="SkipField", ctx=Load()),
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Name(id="set_value", ctx=Load()),
                                                args=[
                                                    Name(id="ret", ctx=Load()),
                                                    Attribute(
                                                        value=Name(
                                                            id="field", ctx=Load()
                                                        ),
                                                        attr="source_attrs",
                                                        ctx=Load(),
                                                    ),
                                                    Name(
                                                        id="validated_value", ctx=Load()
                                                    ),
                                                ],
                                                keywords=[],
                                            )
                                        )
                                    ],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id="errors", ctx=Load()),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id="ValidationError", ctx=Load()),
                                        args=[Name(id="errors", ctx=Load())],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(value=Name(id="ret", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="to_representation",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="instance")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Object instance -> Dict of primitive datatypes.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="ret", ctx=Store())],
                            value=Call(
                                func=Name(id="OrderedDict", ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="fields", ctx=Store())],
                            value=Attribute(
                                value=Name(id="self", ctx=Load()),
                                attr="_readable_fields",
                                ctx=Load(),
                            ),
                        ),
                        For(
                            target=Name(id="field", ctx=Store()),
                            iter=Name(id="fields", ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id="attribute", ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="field", ctx=Load()),
                                                    attr="get_attribute",
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id="instance", ctx=Load())],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id="SkipField", ctx=Load()),
                                            body=[Continue()],
                                        )
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Assign(
                                    targets=[Name(id="check_for_none", ctx=Store())],
                                    value=IfExp(
                                        test=Call(
                                            func=Name(id="isinstance", ctx=Load()),
                                            args=[
                                                Name(id="attribute", ctx=Load()),
                                                Name(id="PKOnlyObject", ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id="attribute", ctx=Load()),
                                            attr="pk",
                                            ctx=Load(),
                                        ),
                                        orelse=Name(id="attribute", ctx=Load()),
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id="check_for_none", ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id="ret", ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(
                                                            id="field", ctx=Load()
                                                        ),
                                                        attr="field_name",
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=Constant(value=None),
                                        )
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id="ret", ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(
                                                            id="field", ctx=Load()
                                                        ),
                                                        attr="field_name",
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="field", ctx=Load()),
                                                    attr="to_representation",
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id="attribute", ctx=Load())],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(value=Name(id="ret", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="validate",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="attrs")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[Return(value=Name(id="attrs", ctx=Load()))],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="__repr__",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="representation", ctx=Load()),
                                    attr="serializer_repr",
                                    ctx=Load(),
                                ),
                                args=[Name(id="self", ctx=Load())],
                                keywords=[
                                    keyword(arg="indent", value=Constant(value=1))
                                ],
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="__iter__",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id="field", ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="fields",
                                        ctx=Load(),
                                    ),
                                    attr="values",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Subscript(
                                            value=Name(id="self", ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id="field", ctx=Load()),
                                                attr="field_name",
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        )
                                    )
                                )
                            ],
                            orelse=[],
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="__getitem__",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="key")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id="field", ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="fields",
                                    ctx=Load(),
                                ),
                                slice=Name(id="key", ctx=Load()),
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id="value", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="data",
                                        ctx=Load(),
                                    ),
                                    attr="get",
                                    ctx=Load(),
                                ),
                                args=[Name(id="key", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="error", ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id="hasattr", ctx=Load()),
                                    args=[
                                        Name(id="self", ctx=Load()),
                                        Constant(value="_errors"),
                                    ],
                                    keywords=[],
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="errors",
                                            ctx=Load(),
                                        ),
                                        attr="get",
                                        ctx=Load(),
                                    ),
                                    args=[Name(id="key", ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Constant(value=None),
                            ),
                        ),
                        If(
                            test=Call(
                                func=Name(id="isinstance", ctx=Load()),
                                args=[
                                    Name(id="field", ctx=Load()),
                                    Name(id="Serializer", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id="NestedBoundField", ctx=Load()),
                                        args=[
                                            Name(id="field", ctx=Load()),
                                            Name(id="value", ctx=Load()),
                                            Name(id="error", ctx=Load()),
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id="isinstance", ctx=Load()),
                                args=[
                                    Name(id="field", ctx=Load()),
                                    Name(id="JSONField", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id="JSONBoundField", ctx=Load()),
                                        args=[
                                            Name(id="field", ctx=Load()),
                                            Name(id="value", ctx=Load()),
                                            Name(id="error", ctx=Load()),
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id="BoundField", ctx=Load()),
                                args=[
                                    Name(id="field", ctx=Load()),
                                    Name(id="value", ctx=Load()),
                                    Name(id="error", ctx=Load()),
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="data",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id="ret", ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id="super", ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                                attr="data",
                                ctx=Load(),
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id="ReturnDict", ctx=Load()),
                                args=[Name(id="ret", ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg="serializer",
                                        value=Name(id="self", ctx=Load()),
                                    )
                                ],
                            )
                        ),
                    ],
                    decorator_list=[Name(id="property", ctx=Load())],
                ),
                FunctionDef(
                    name="errors",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id="ret", ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id="super", ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                                attr="errors",
                                ctx=Load(),
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id="isinstance", ctx=Load()),
                                        args=[
                                            Name(id="ret", ctx=Load()),
                                            Name(id="list", ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id="len", ctx=Load()),
                                            args=[Name(id="ret", ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id="getattr", ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id="ret", ctx=Load()),
                                                    slice=Constant(value=0),
                                                    ctx=Load(),
                                                ),
                                                Constant(value="code"),
                                                Constant(value=None),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value="null")],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="detail", ctx=Store())],
                                    value=Call(
                                        func=Name(id="ErrorDetail", ctx=Load()),
                                        args=[Constant(value="No data provided")],
                                        keywords=[
                                            keyword(
                                                arg="code", value=Constant(value="null")
                                            )
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id="ret", ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(
                                                    id="api_settings", ctx=Load()
                                                ),
                                                attr="NON_FIELD_ERRORS_KEY",
                                                ctx=Load(),
                                            )
                                        ],
                                        values=[
                                            List(
                                                elts=[Name(id="detail", ctx=Load())],
                                                ctx=Load(),
                                            )
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id="ReturnDict", ctx=Load()),
                                args=[Name(id="ret", ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg="serializer",
                                        value=Name(id="self", ctx=Load()),
                                    )
                                ],
                            )
                        ),
                    ],
                    decorator_list=[Name(id="property", ctx=Load())],
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name="ListSerializer",
            bases=[Name(id="BaseSerializer", ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id="child", ctx=Store())], value=Constant(value=None)
                ),
                Assign(
                    targets=[Name(id="many", ctx=Store())], value=Constant(value=True)
                ),
                Assign(
                    targets=[Name(id="default_error_messages", ctx=Store())],
                    value=Dict(
                        keys=[Constant(value="not_a_list"), Constant(value="empty")],
                        values=[
                            Call(
                                func=Name(id="_", ctx=Load()),
                                args=[
                                    Constant(
                                        value='Expected a list of items but got type "{input_type}".'
                                    )
                                ],
                                keywords=[],
                            ),
                            Call(
                                func=Name(id="_", ctx=Load()),
                                args=[Constant(value="This list may not be empty.")],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
                FunctionDef(
                    name="__init__",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        vararg=arg(arg="args"),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg="kwargs"),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="child",
                                    ctx=Store(),
                                )
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="kwargs", ctx=Load()),
                                    attr="pop",
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="child"),
                                    Call(
                                        func=Attribute(
                                            value=Name(id="copy", ctx=Load()),
                                            attr="deepcopy",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id="self", ctx=Load()),
                                                attr="child",
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="allow_empty",
                                    ctx=Store(),
                                )
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="kwargs", ctx=Load()),
                                    attr="pop",
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="allow_empty"),
                                    Constant(value=True),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assert(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="child",
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None)],
                            ),
                            msg=Constant(value="`child` is a required argument."),
                        ),
                        Assert(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id="inspect", ctx=Load()),
                                        attr="isclass",
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="child",
                                            ctx=Load(),
                                        )
                                    ],
                                    keywords=[],
                                ),
                            ),
                            msg=Constant(value="`child` has not been instantiated."),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id="super", ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr="__init__",
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id="args", ctx=Load()), ctx=Load()
                                    )
                                ],
                                keywords=[keyword(value=Name(id="kwargs", ctx=Load()))],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="child",
                                        ctx=Load(),
                                    ),
                                    attr="bind",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(arg="field_name", value=Constant(value="")),
                                    keyword(
                                        arg="parent", value=Name(id="self", ctx=Load())
                                    ),
                                ],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_initial",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id="hasattr", ctx=Load()),
                                args=[
                                    Name(id="self", ctx=Load()),
                                    Constant(value="initial_data"),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="to_representation",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id="self", ctx=Load()),
                                                attr="initial_data",
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(value=List(elts=[], ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_value",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="dictionary")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Given the input dictionary, return the field value.\n        "
                            )
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id="html", ctx=Load()),
                                    attr="is_html_input",
                                    ctx=Load(),
                                ),
                                args=[Name(id="dictionary", ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="html", ctx=Load()),
                                            attr="parse_html_list",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="dictionary", ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg="prefix",
                                                value=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="field_name",
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg="default",
                                                value=Name(id="empty", ctx=Load()),
                                            ),
                                        ],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="dictionary", ctx=Load()),
                                    attr="get",
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="field_name",
                                        ctx=Load(),
                                    ),
                                    Name(id="empty", ctx=Load()),
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="run_validation",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="data")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[Name(id="empty", ctx=Load())],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        We override the default `run_validation`, because the validation\n        performed by validators and the `.validate()` method should\n        be coerced into an error dictionary with a 'non_fields_error' key.\n        "
                            )
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id="is_empty_value", ctx=Store()),
                                        Name(id="data", ctx=Store()),
                                    ],
                                    ctx=Store(),
                                )
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="validate_empty_values",
                                    ctx=Load(),
                                ),
                                args=[Name(id="data", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id="is_empty_value", ctx=Load()),
                            body=[Return(value=Name(id="data", ctx=Load()))],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="value", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="to_internal_value",
                                    ctx=Load(),
                                ),
                                args=[Name(id="data", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="run_validators",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="value", ctx=Load())],
                                        keywords=[],
                                    )
                                ),
                                Assign(
                                    targets=[Name(id="value", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="validate",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="value", ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assert(
                                    test=Compare(
                                        left=Name(id="value", ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None)],
                                    ),
                                    msg=Constant(
                                        value=".validate() should return the validated data"
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id="ValidationError", ctx=Load()),
                                            Name(
                                                id="DjangoValidationError", ctx=Load()
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name="exc",
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(
                                                    id="ValidationError", ctx=Load()
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg="detail",
                                                        value=Call(
                                                            func=Name(
                                                                id="as_serializer_error",
                                                                ctx=Load(),
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
                                            )
                                        )
                                    ],
                                )
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(value=Name(id="value", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="to_internal_value",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="data")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        List of dicts of native values <- List of dicts of primitive datatypes.\n        "
                            )
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id="html", ctx=Load()),
                                    attr="is_html_input",
                                    ctx=Load(),
                                ),
                                args=[Name(id="data", ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="data", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="html", ctx=Load()),
                                            attr="parse_html_list",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="data", ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg="default",
                                                value=List(elts=[], ctx=Load()),
                                            )
                                        ],
                                    ),
                                )
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="isinstance", ctx=Load()),
                                    args=[
                                        Name(id="data", ctx=Load()),
                                        Name(id="list", ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="message", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="error_messages",
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value="not_a_list"),
                                                ctx=Load(),
                                            ),
                                            attr="format",
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg="input_type",
                                                value=Attribute(
                                                    value=Call(
                                                        func=Name(
                                                            id="type", ctx=Load()
                                                        ),
                                                        args=[
                                                            Name(id="data", ctx=Load())
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr="__name__",
                                                    ctx=Load(),
                                                ),
                                            )
                                        ],
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id="ValidationError", ctx=Load()),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Attribute(
                                                        value=Name(
                                                            id="api_settings",
                                                            ctx=Load(),
                                                        ),
                                                        attr="NON_FIELD_ERRORS_KEY",
                                                        ctx=Load(),
                                                    )
                                                ],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Name(
                                                                id="message", ctx=Load()
                                                            )
                                                        ],
                                                        ctx=Load(),
                                                    )
                                                ],
                                            )
                                        ],
                                        keywords=[
                                            keyword(
                                                arg="code",
                                                value=Constant(value="not_a_list"),
                                            )
                                        ],
                                    )
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="allow_empty",
                                            ctx=Load(),
                                        ),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id="len", ctx=Load()),
                                            args=[Name(id="data", ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="message", ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="error_messages",
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value="empty"),
                                        ctx=Load(),
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id="ValidationError", ctx=Load()),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Attribute(
                                                        value=Name(
                                                            id="api_settings",
                                                            ctx=Load(),
                                                        ),
                                                        attr="NON_FIELD_ERRORS_KEY",
                                                        ctx=Load(),
                                                    )
                                                ],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Name(
                                                                id="message", ctx=Load()
                                                            )
                                                        ],
                                                        ctx=Load(),
                                                    )
                                                ],
                                            )
                                        ],
                                        keywords=[
                                            keyword(
                                                arg="code",
                                                value=Constant(value="empty"),
                                            )
                                        ],
                                    )
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="ret", ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                        ),
                        Assign(
                            targets=[Name(id="errors", ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                        ),
                        For(
                            target=Name(id="item", ctx=Store()),
                            iter=Name(id="data", ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id="validated", ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(
                                                            id="self", ctx=Load()
                                                        ),
                                                        attr="child",
                                                        ctx=Load(),
                                                    ),
                                                    attr="run_validation",
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id="item", ctx=Load())],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id="ValidationError", ctx=Load()),
                                            name="exc",
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(
                                                                id="errors", ctx=Load()
                                                            ),
                                                            attr="append",
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(
                                                                    id="exc", ctx=Load()
                                                                ),
                                                                attr="detail",
                                                                ctx=Load(),
                                                            )
                                                        ],
                                                        keywords=[],
                                                    )
                                                )
                                            ],
                                        )
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="ret", ctx=Load()),
                                                    attr="append",
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id="validated", ctx=Load())],
                                                keywords=[],
                                            )
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="errors", ctx=Load()),
                                                    attr="append",
                                                    ctx=Load(),
                                                ),
                                                args=[Dict(keys=[], values=[])],
                                                keywords=[],
                                            )
                                        ),
                                    ],
                                    finalbody=[],
                                )
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id="any", ctx=Load()),
                                args=[Name(id="errors", ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id="ValidationError", ctx=Load()),
                                        args=[Name(id="errors", ctx=Load())],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(value=Name(id="ret", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="to_representation",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="data")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        List of object instances -> List of dicts of primitive datatypes.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="iterable", ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id="isinstance", ctx=Load()),
                                    args=[
                                        Name(id="data", ctx=Load()),
                                        Attribute(
                                            value=Name(id="models", ctx=Load()),
                                            attr="Manager",
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id="data", ctx=Load()),
                                        attr="all",
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                orelse=Name(id="data", ctx=Load()),
                            ),
                        ),
                        Return(
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="child",
                                            ctx=Load(),
                                        ),
                                        attr="to_representation",
                                        ctx=Load(),
                                    ),
                                    args=[Name(id="item", ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id="item", ctx=Store()),
                                        iter=Name(id="iterable", ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    )
                                ],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="validate",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="attrs")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[Return(value=Name(id="attrs", ctx=Load()))],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="update",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="instance"),
                            arg(arg="validated_data"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id="NotImplementedError", ctx=Load()),
                                args=[
                                    Constant(
                                        value="Serializers with many=True do not support multiple update by default, only multiple create. For updates it is unclear how to deal with insertions and deletions. If you need to support multiple update, use a `ListSerializer` class and override `.update()` so you can specify the behavior exactly."
                                    )
                                ],
                                keywords=[],
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="create",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="validated_data")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="child",
                                            ctx=Load(),
                                        ),
                                        attr="create",
                                        ctx=Load(),
                                    ),
                                    args=[Name(id="attrs", ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id="attrs", ctx=Store()),
                                        iter=Name(id="validated_data", ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    )
                                ],
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="save",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg="kwargs"),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Save and return a list of object instances.\n        "
                            )
                        ),
                        Assert(
                            test=Compare(
                                left=Constant(value="commit"),
                                ops=[NotIn()],
                                comparators=[Name(id="kwargs", ctx=Load())],
                            ),
                            msg=Constant(
                                value="'commit' is not a valid keyword argument to the 'save()' method. If you need to access data before committing to the database then inspect 'serializer.validated_data' instead. You can also pass additional keyword arguments to 'save()' if you need to set extra attributes on the saved model instance. For example: 'serializer.save(owner=request.user)'.'"
                            ),
                        ),
                        Assign(
                            targets=[Name(id="validated_data", ctx=Store())],
                            value=ListComp(
                                elt=Dict(
                                    keys=[None, None],
                                    values=[
                                        Name(id="attrs", ctx=Load()),
                                        Name(id="kwargs", ctx=Load()),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id="attrs", ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="validated_data",
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    )
                                ],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="instance",
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="instance",
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="update",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id="self", ctx=Load()),
                                                attr="instance",
                                                ctx=Load(),
                                            ),
                                            Name(id="validated_data", ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assert(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="instance",
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None)],
                                    ),
                                    msg=Constant(
                                        value="`update()` did not return an object instance."
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="instance",
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="create",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="validated_data", ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assert(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="instance",
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None)],
                                    ),
                                    msg=Constant(
                                        value="`create()` did not return an object instance."
                                    ),
                                ),
                            ],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id="self", ctx=Load()),
                                attr="instance",
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="is_valid",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="raise_exception")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[Constant(value=False)],
                    ),
                    body=[
                        Assert(
                            test=Call(
                                func=Name(id="hasattr", ctx=Load()),
                                args=[
                                    Name(id="self", ctx=Load()),
                                    Constant(value="initial_data"),
                                ],
                                keywords=[],
                            ),
                            msg=Constant(
                                value="Cannot call `.is_valid()` as no `data=` keyword argument was passed when instantiating the serializer instance."
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="hasattr", ctx=Load()),
                                    args=[
                                        Name(id="self", ctx=Load()),
                                        Constant(value="_validated_data"),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="_validated_data",
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="run_validation",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(
                                                            id="self", ctx=Load()
                                                        ),
                                                        attr="initial_data",
                                                        ctx=Load(),
                                                    )
                                                ],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id="ValidationError", ctx=Load()),
                                            name="exc",
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="_validated_data",
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=List(elts=[], ctx=Load()),
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="_errors",
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Attribute(
                                                        value=Name(
                                                            id="exc", ctx=Load()
                                                        ),
                                                        attr="detail",
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        )
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="_errors",
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=List(elts=[], ctx=Load()),
                                        )
                                    ],
                                    finalbody=[],
                                )
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="_errors",
                                        ctx=Load(),
                                    ),
                                    Name(id="raise_exception", ctx=Load()),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id="ValidationError", ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id="self", ctx=Load()),
                                                attr="errors",
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="bool", ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="_errors",
                                            ctx=Load(),
                                        )
                                    ],
                                    keywords=[],
                                ),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="__repr__",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="representation", ctx=Load()),
                                    attr="list_repr",
                                    ctx=Load(),
                                ),
                                args=[Name(id="self", ctx=Load())],
                                keywords=[
                                    keyword(arg="indent", value=Constant(value=1))
                                ],
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="data",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id="ret", ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id="super", ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                                attr="data",
                                ctx=Load(),
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id="ReturnList", ctx=Load()),
                                args=[Name(id="ret", ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg="serializer",
                                        value=Name(id="self", ctx=Load()),
                                    )
                                ],
                            )
                        ),
                    ],
                    decorator_list=[Name(id="property", ctx=Load())],
                ),
                FunctionDef(
                    name="errors",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id="ret", ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id="super", ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                                attr="errors",
                                ctx=Load(),
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id="isinstance", ctx=Load()),
                                        args=[
                                            Name(id="ret", ctx=Load()),
                                            Name(id="list", ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id="len", ctx=Load()),
                                            args=[Name(id="ret", ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id="getattr", ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id="ret", ctx=Load()),
                                                    slice=Constant(value=0),
                                                    ctx=Load(),
                                                ),
                                                Constant(value="code"),
                                                Constant(value=None),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value="null")],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="detail", ctx=Store())],
                                    value=Call(
                                        func=Name(id="ErrorDetail", ctx=Load()),
                                        args=[Constant(value="No data provided")],
                                        keywords=[
                                            keyword(
                                                arg="code", value=Constant(value="null")
                                            )
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id="ret", ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(
                                                    id="api_settings", ctx=Load()
                                                ),
                                                attr="NON_FIELD_ERRORS_KEY",
                                                ctx=Load(),
                                            )
                                        ],
                                        values=[
                                            List(
                                                elts=[Name(id="detail", ctx=Load())],
                                                ctx=Load(),
                                            )
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id="isinstance", ctx=Load()),
                                args=[
                                    Name(id="ret", ctx=Load()),
                                    Name(id="dict", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id="ReturnDict", ctx=Load()),
                                        args=[Name(id="ret", ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg="serializer",
                                                value=Name(id="self", ctx=Load()),
                                            )
                                        ],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id="ReturnList", ctx=Load()),
                                args=[Name(id="ret", ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg="serializer",
                                        value=Name(id="self", ctx=Load()),
                                    )
                                ],
                            )
                        ),
                    ],
                    decorator_list=[Name(id="property", ctx=Load())],
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name="raise_errors_on_nested_writes",
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg="method_name"),
                    arg(arg="serializer"),
                    arg(arg="validated_data"),
                ],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(
                        value="\n    Give explicit errors when users attempt to pass writable nested data.\n\n    If we don't do this explicitly they'd get a less helpful error when\n    calling `.save()` on the serializer.\n\n    We don't *automatically* support these sorts of nested writes because\n    there are too many ambiguities to define a default behavior.\n\n    Eg. Suppose we have a `UserSerializer` with a nested profile. How should\n    we handle the case of an update, where the `profile` relationship does\n    not exist? Any of the following might be valid:\n\n    * Raise an application error.\n    * Silently ignore the nested part of the update.\n    * Automatically create a profile instance.\n    "
                    )
                ),
                Assign(
                    targets=[Name(id="ModelClass", ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id="serializer", ctx=Load()),
                            attr="Meta",
                            ctx=Load(),
                        ),
                        attr="model",
                        ctx=Load(),
                    ),
                ),
                Assign(
                    targets=[Name(id="model_field_info", ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id="model_meta", ctx=Load()),
                            attr="get_field_info",
                            ctx=Load(),
                        ),
                        args=[Name(id="ModelClass", ctx=Load())],
                        keywords=[],
                    ),
                ),
                Assert(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id="any", ctx=Load()),
                            args=[
                                GeneratorExp(
                                    elt=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id="isinstance", ctx=Load()),
                                                args=[
                                                    Name(id="field", ctx=Load()),
                                                    Name(
                                                        id="BaseSerializer", ctx=Load()
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id="field", ctx=Load()),
                                                    attr="source",
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Name(
                                                        id="validated_data", ctx=Load()
                                                    )
                                                ],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id="field", ctx=Load()),
                                                    attr="source",
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(
                                                            id="model_field_info",
                                                            ctx=Load(),
                                                        ),
                                                        attr="relations",
                                                        ctx=Load(),
                                                    )
                                                ],
                                            ),
                                            Call(
                                                func=Name(id="isinstance", ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(
                                                            id="validated_data",
                                                            ctx=Load(),
                                                        ),
                                                        slice=Attribute(
                                                            value=Name(
                                                                id="field", ctx=Load()
                                                            ),
                                                            attr="source",
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Name(id="list", ctx=Load()),
                                                            Name(id="dict", ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id="field", ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id="serializer", ctx=Load()),
                                                attr="_writable_fields",
                                                ctx=Load(),
                                            ),
                                            ifs=[],
                                            is_async=0,
                                        )
                                    ],
                                )
                            ],
                            keywords=[],
                        ),
                    ),
                    msg=Call(
                        func=Attribute(
                            value=Constant(
                                value="The `.{method_name}()` method does not support writable nested fields by default.\nWrite an explicit `.{method_name}()` method for serializer `{module}.{class_name}`, or set `read_only=True` on nested serializer fields."
                            ),
                            attr="format",
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg="method_name",
                                value=Name(id="method_name", ctx=Load()),
                            ),
                            keyword(
                                arg="module",
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id="serializer", ctx=Load()),
                                        attr="__class__",
                                        ctx=Load(),
                                    ),
                                    attr="__module__",
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg="class_name",
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id="serializer", ctx=Load()),
                                        attr="__class__",
                                        ctx=Load(),
                                    ),
                                    attr="__name__",
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                ),
                Assert(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id="any", ctx=Load()),
                            args=[
                                GeneratorExp(
                                    elt=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id="len", ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(
                                                                id="field", ctx=Load()
                                                            ),
                                                            attr="source_attrs",
                                                            ctx=Load(),
                                                        )
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1)],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(
                                                            id="field", ctx=Load()
                                                        ),
                                                        attr="source_attrs",
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Name(
                                                        id="validated_data", ctx=Load()
                                                    )
                                                ],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(
                                                            id="field", ctx=Load()
                                                        ),
                                                        attr="source_attrs",
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(
                                                            id="model_field_info",
                                                            ctx=Load(),
                                                        ),
                                                        attr="relations",
                                                        ctx=Load(),
                                                    )
                                                ],
                                            ),
                                            Call(
                                                func=Name(id="isinstance", ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(
                                                            id="validated_data",
                                                            ctx=Load(),
                                                        ),
                                                        slice=Subscript(
                                                            value=Attribute(
                                                                value=Name(
                                                                    id="field",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="source_attrs",
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Name(id="list", ctx=Load()),
                                                            Name(id="dict", ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id="field", ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id="serializer", ctx=Load()),
                                                attr="_writable_fields",
                                                ctx=Load(),
                                            ),
                                            ifs=[],
                                            is_async=0,
                                        )
                                    ],
                                )
                            ],
                            keywords=[],
                        ),
                    ),
                    msg=Call(
                        func=Attribute(
                            value=Constant(
                                value="The `.{method_name}()` method does not support writable dotted-source fields by default.\nWrite an explicit `.{method_name}()` method for serializer `{module}.{class_name}`, or set `read_only=True` on dotted-source serializer fields."
                            ),
                            attr="format",
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg="method_name",
                                value=Name(id="method_name", ctx=Load()),
                            ),
                            keyword(
                                arg="module",
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id="serializer", ctx=Load()),
                                        attr="__class__",
                                        ctx=Load(),
                                    ),
                                    attr="__module__",
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg="class_name",
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id="serializer", ctx=Load()),
                                        attr="__class__",
                                        ctx=Load(),
                                    ),
                                    attr="__name__",
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name="ModelSerializer",
            bases=[Name(id="Serializer", ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(
                        value="\n    A `ModelSerializer` is just a regular `Serializer`, except that:\n\n    * A set of default fields are automatically populated.\n    * A set of default validators are automatically populated.\n    * Default `.create()` and `.update()` implementations are provided.\n\n    The process of automatically determining a set of serializer fields\n    based on the model fields is reasonably complex, but you almost certainly\n    don't need to dig into the implementation.\n\n    If the `ModelSerializer` class *doesn't* generate the set of fields that\n    you need you should either declare the extra/differing fields explicitly on\n    the serializer class, or simply use a `Serializer` class.\n    "
                    )
                ),
                Assign(
                    targets=[Name(id="serializer_field_mapping", ctx=Store())],
                    value=Dict(
                        keys=[
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="AutoField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="BigIntegerField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="BooleanField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="CharField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="CommaSeparatedIntegerField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="DateField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="DateTimeField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="DecimalField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="DurationField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="EmailField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="Field",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="FileField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="FloatField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="ImageField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="IntegerField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="NullBooleanField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="PositiveIntegerField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="PositiveSmallIntegerField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="SlugField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="SmallIntegerField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="TextField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="TimeField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="URLField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="UUIDField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="GenericIPAddressField",
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id="models", ctx=Load()),
                                attr="FilePathField",
                                ctx=Load(),
                            ),
                        ],
                        values=[
                            Name(id="IntegerField", ctx=Load()),
                            Name(id="IntegerField", ctx=Load()),
                            Name(id="BooleanField", ctx=Load()),
                            Name(id="CharField", ctx=Load()),
                            Name(id="CharField", ctx=Load()),
                            Name(id="DateField", ctx=Load()),
                            Name(id="DateTimeField", ctx=Load()),
                            Name(id="DecimalField", ctx=Load()),
                            Name(id="DurationField", ctx=Load()),
                            Name(id="EmailField", ctx=Load()),
                            Name(id="ModelField", ctx=Load()),
                            Name(id="FileField", ctx=Load()),
                            Name(id="FloatField", ctx=Load()),
                            Name(id="ImageField", ctx=Load()),
                            Name(id="IntegerField", ctx=Load()),
                            Name(id="BooleanField", ctx=Load()),
                            Name(id="IntegerField", ctx=Load()),
                            Name(id="IntegerField", ctx=Load()),
                            Name(id="SlugField", ctx=Load()),
                            Name(id="IntegerField", ctx=Load()),
                            Name(id="CharField", ctx=Load()),
                            Name(id="TimeField", ctx=Load()),
                            Name(id="URLField", ctx=Load()),
                            Name(id="UUIDField", ctx=Load()),
                            Name(id="IPAddressField", ctx=Load()),
                            Name(id="FilePathField", ctx=Load()),
                        ],
                    ),
                ),
                If(
                    test=Call(
                        func=Name(id="hasattr", ctx=Load()),
                        args=[
                            Name(id="models", ctx=Load()),
                            Constant(value="JSONField"),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(
                                        id="serializer_field_mapping", ctx=Load()
                                    ),
                                    slice=Attribute(
                                        value=Name(id="models", ctx=Load()),
                                        attr="JSONField",
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id="JSONField", ctx=Load()),
                        )
                    ],
                    orelse=[],
                ),
                If(
                    test=Name(id="postgres_fields", ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(
                                        id="serializer_field_mapping", ctx=Load()
                                    ),
                                    slice=Attribute(
                                        value=Name(id="postgres_fields", ctx=Load()),
                                        attr="HStoreField",
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id="HStoreField", ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(
                                        id="serializer_field_mapping", ctx=Load()
                                    ),
                                    slice=Attribute(
                                        value=Name(id="postgres_fields", ctx=Load()),
                                        attr="ArrayField",
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id="ListField", ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(
                                        id="serializer_field_mapping", ctx=Load()
                                    ),
                                    slice=Attribute(
                                        value=Name(id="postgres_fields", ctx=Load()),
                                        attr="JSONField",
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id="JSONField", ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id="serializer_related_field", ctx=Store())],
                    value=Name(id="PrimaryKeyRelatedField", ctx=Load()),
                ),
                Assign(
                    targets=[Name(id="serializer_related_to_field", ctx=Store())],
                    value=Name(id="SlugRelatedField", ctx=Load()),
                ),
                Assign(
                    targets=[Name(id="serializer_url_field", ctx=Store())],
                    value=Name(id="HyperlinkedIdentityField", ctx=Load()),
                ),
                Assign(
                    targets=[Name(id="serializer_choice_field", ctx=Store())],
                    value=Name(id="ChoiceField", ctx=Load()),
                ),
                Assign(
                    targets=[Name(id="url_field_name", ctx=Store())],
                    value=Constant(value=None),
                ),
                FunctionDef(
                    name="create",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self"), arg(arg="validated_data")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        We have a bit of extra checking around this in order to provide\n        descriptive messages when something goes wrong, but this method is\n        essentially just:\n\n            return ExampleModel.objects.create(**validated_data)\n\n        If there are many to many fields present on the instance then they\n        cannot be set until the model is instantiated, in which case the\n        implementation is like so:\n\n            example_relationship = validated_data.pop('example_relationship')\n            instance = ExampleModel.objects.create(**validated_data)\n            instance.example_relationship = example_relationship\n            return instance\n\n        The default implementation also does not handle nested relationships.\n        If you want to support writable nested relationships you'll need\n        to write an explicit `.create()` method.\n        "
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Name(
                                    id="raise_errors_on_nested_writes", ctx=Load()
                                ),
                                args=[
                                    Constant(value="create"),
                                    Name(id="self", ctx=Load()),
                                    Name(id="validated_data", ctx=Load()),
                                ],
                                keywords=[],
                            )
                        ),
                        Assign(
                            targets=[Name(id="ModelClass", ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="Meta",
                                    ctx=Load(),
                                ),
                                attr="model",
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id="info", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="model_meta", ctx=Load()),
                                    attr="get_field_info",
                                    ctx=Load(),
                                ),
                                args=[Name(id="ModelClass", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="many_to_many", ctx=Store())],
                            value=Dict(keys=[], values=[]),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id="field_name", ctx=Store()),
                                    Name(id="relation_info", ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id="info", ctx=Load()),
                                        attr="relations",
                                        ctx=Load(),
                                    ),
                                    attr="items",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(
                                                    id="relation_info", ctx=Load()
                                                ),
                                                attr="to_many",
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Name(id="field_name", ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Name(
                                                        id="validated_data", ctx=Load()
                                                    )
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(
                                                        id="many_to_many", ctx=Load()
                                                    ),
                                                    slice=Name(
                                                        id="field_name", ctx=Load()
                                                    ),
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(
                                                        id="validated_data", ctx=Load()
                                                    ),
                                                    attr="pop",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id="field_name", ctx=Load())
                                                ],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                    orelse=[],
                                )
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id="instance", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id="ModelClass", ctx=Load()),
                                                attr="_default_manager",
                                                ctx=Load(),
                                            ),
                                            attr="create",
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                value=Name(
                                                    id="validated_data", ctx=Load()
                                                )
                                            )
                                        ],
                                    ),
                                )
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id="TypeError", ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id="tb", ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(
                                                        id="traceback", ctx=Load()
                                                    ),
                                                    attr="format_exc",
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id="msg", ctx=Store())],
                                            value=BinOp(
                                                left=Constant(
                                                    value="Got a `TypeError` when calling `%s.%s.create()`. This may be because you have a writable field on the serializer class that is not a valid argument to `%s.%s.create()`. You may need to make the field read-only, or override the %s.create() method to handle this correctly.\nOriginal exception was:\n %s"
                                                ),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(
                                                                id="ModelClass",
                                                                ctx=Load(),
                                                            ),
                                                            attr="__name__",
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(
                                                                    id="ModelClass",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="_default_manager",
                                                                ctx=Load(),
                                                            ),
                                                            attr="name",
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(
                                                                id="ModelClass",
                                                                ctx=Load(),
                                                            ),
                                                            attr="__name__",
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(
                                                                    id="ModelClass",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="_default_manager",
                                                                ctx=Load(),
                                                            ),
                                                            attr="name",
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(
                                                                    id="self",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="__class__",
                                                                ctx=Load(),
                                                            ),
                                                            attr="__name__",
                                                            ctx=Load(),
                                                        ),
                                                        Name(id="tb", ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id="TypeError", ctx=Load()),
                                                args=[Name(id="msg", ctx=Load())],
                                                keywords=[],
                                            )
                                        ),
                                    ],
                                )
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=Name(id="many_to_many", ctx=Load()),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id="field_name", ctx=Store()),
                                            Name(id="value", ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id="many_to_many", ctx=Load()),
                                            attr="items",
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id="field", ctx=Store())],
                                            value=Call(
                                                func=Name(id="getattr", ctx=Load()),
                                                args=[
                                                    Name(id="instance", ctx=Load()),
                                                    Name(id="field_name", ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="field", ctx=Load()),
                                                    attr="set",
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id="value", ctx=Load())],
                                                keywords=[],
                                            )
                                        ),
                                    ],
                                    orelse=[],
                                )
                            ],
                            orelse=[],
                        ),
                        Return(value=Name(id="instance", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="update",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="instance"),
                            arg(arg="validated_data"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(
                                    id="raise_errors_on_nested_writes", ctx=Load()
                                ),
                                args=[
                                    Constant(value="update"),
                                    Name(id="self", ctx=Load()),
                                    Name(id="validated_data", ctx=Load()),
                                ],
                                keywords=[],
                            )
                        ),
                        Assign(
                            targets=[Name(id="info", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="model_meta", ctx=Load()),
                                    attr="get_field_info",
                                    ctx=Load(),
                                ),
                                args=[Name(id="instance", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="m2m_fields", ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id="attr", ctx=Store()),
                                    Name(id="value", ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id="validated_data", ctx=Load()),
                                    attr="items",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id="attr", ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(
                                                            id="info", ctx=Load()
                                                        ),
                                                        attr="relations",
                                                        ctx=Load(),
                                                    )
                                                ],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(
                                                            id="info", ctx=Load()
                                                        ),
                                                        attr="relations",
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id="attr", ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr="to_many",
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(
                                                        id="m2m_fields", ctx=Load()
                                                    ),
                                                    attr="append",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id="attr", ctx=Load()),
                                                            Name(
                                                                id="value", ctx=Load()
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    )
                                                ],
                                                keywords=[],
                                            )
                                        )
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Name(id="setattr", ctx=Load()),
                                                args=[
                                                    Name(id="instance", ctx=Load()),
                                                    Name(id="attr", ctx=Load()),
                                                    Name(id="value", ctx=Load()),
                                                ],
                                                keywords=[],
                                            )
                                        )
                                    ],
                                )
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="instance", ctx=Load()),
                                    attr="save",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            )
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id="attr", ctx=Store()),
                                    Name(id="value", ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id="m2m_fields", ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id="field", ctx=Store())],
                                    value=Call(
                                        func=Name(id="getattr", ctx=Load()),
                                        args=[
                                            Name(id="instance", ctx=Load()),
                                            Name(id="attr", ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="field", ctx=Load()),
                                            attr="set",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="value", ctx=Load())],
                                        keywords=[],
                                    )
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(value=Name(id="instance", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_fields",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Return the dict of field names -> field instances that should be\n        used for `self.fields` when instantiating the serializer.\n        "
                            )
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="url_field_name",
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="url_field_name",
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Attribute(
                                        value=Name(id="api_settings", ctx=Load()),
                                        attr="URL_FIELD_NAME",
                                        ctx=Load(),
                                    ),
                                )
                            ],
                            orelse=[],
                        ),
                        Assert(
                            test=Call(
                                func=Name(id="hasattr", ctx=Load()),
                                args=[
                                    Name(id="self", ctx=Load()),
                                    Constant(value="Meta"),
                                ],
                                keywords=[],
                            ),
                            msg=Call(
                                func=Attribute(
                                    value=Constant(
                                        value='Class {serializer_class} missing "Meta" attribute'
                                    ),
                                    attr="format",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg="serializer_class",
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id="self", ctx=Load()),
                                                attr="__class__",
                                                ctx=Load(),
                                            ),
                                            attr="__name__",
                                            ctx=Load(),
                                        ),
                                    )
                                ],
                            ),
                        ),
                        Assert(
                            test=Call(
                                func=Name(id="hasattr", ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="Meta",
                                        ctx=Load(),
                                    ),
                                    Constant(value="model"),
                                ],
                                keywords=[],
                            ),
                            msg=Call(
                                func=Attribute(
                                    value=Constant(
                                        value='Class {serializer_class} missing "Meta.model" attribute'
                                    ),
                                    attr="format",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg="serializer_class",
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id="self", ctx=Load()),
                                                attr="__class__",
                                                ctx=Load(),
                                            ),
                                            attr="__name__",
                                            ctx=Load(),
                                        ),
                                    )
                                ],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id="model_meta", ctx=Load()),
                                    attr="is_abstract_model",
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="Meta",
                                            ctx=Load(),
                                        ),
                                        attr="model",
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id="ValueError", ctx=Load()),
                                        args=[
                                            Constant(
                                                value="Cannot use ModelSerializer with Abstract Models."
                                            )
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="declared_fields", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="copy", ctx=Load()),
                                    attr="deepcopy",
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="_declared_fields",
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="model", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="Meta",
                                        ctx=Load(),
                                    ),
                                    Constant(value="model"),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="depth", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="Meta",
                                        ctx=Load(),
                                    ),
                                    Constant(value="depth"),
                                    Constant(value=0),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id="depth", ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None)],
                            ),
                            body=[
                                Assert(
                                    test=Compare(
                                        left=Name(id="depth", ctx=Load()),
                                        ops=[GtE()],
                                        comparators=[Constant(value=0)],
                                    ),
                                    msg=Constant(value="'depth' may not be negative."),
                                ),
                                Assert(
                                    test=Compare(
                                        left=Name(id="depth", ctx=Load()),
                                        ops=[LtE()],
                                        comparators=[Constant(value=10)],
                                    ),
                                    msg=Constant(
                                        value="'depth' may not be greater than 10."
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="info", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="model_meta", ctx=Load()),
                                    attr="get_field_info",
                                    ctx=Load(),
                                ),
                                args=[Name(id="model", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="field_names", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="get_field_names",
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id="declared_fields", ctx=Load()),
                                    Name(id="info", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="extra_kwargs", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="get_extra_kwargs",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id="extra_kwargs", ctx=Store()),
                                        Name(id="hidden_fields", ctx=Store()),
                                    ],
                                    ctx=Store(),
                                )
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="get_uniqueness_extra_kwargs",
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id="field_names", ctx=Load()),
                                    Name(id="declared_fields", ctx=Load()),
                                    Name(id="extra_kwargs", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="fields", ctx=Store())],
                            value=Call(
                                func=Name(id="OrderedDict", ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id="field_name", ctx=Store()),
                            iter=Name(id="field_names", ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id="field_name", ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Name(id="declared_fields", ctx=Load())
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id="fields", ctx=Load()),
                                                    slice=Name(
                                                        id="field_name", ctx=Load()
                                                    ),
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=Subscript(
                                                value=Name(
                                                    id="declared_fields", ctx=Load()
                                                ),
                                                slice=Name(id="field_name", ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Name(id="extra_field_kwargs", ctx=Store())
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="extra_kwargs", ctx=Load()),
                                            attr="get",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id="field_name", ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id="source", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(
                                                id="extra_field_kwargs", ctx=Load()
                                            ),
                                            attr="get",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="source"),
                                            Constant(value="*"),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id="source", ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value="*")],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id="source", ctx=Store())],
                                            value=Name(id="field_name", ctx=Load()),
                                        )
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id="field_class", ctx=Store()),
                                                Name(id="field_kwargs", ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="build_field",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id="source", ctx=Load()),
                                            Name(id="info", ctx=Load()),
                                            Name(id="model", ctx=Load()),
                                            Name(id="depth", ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id="field_kwargs", ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="include_extra_kwargs",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id="field_kwargs", ctx=Load()),
                                            Name(id="extra_field_kwargs", ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id="fields", ctx=Load()),
                                            slice=Name(id="field_name", ctx=Load()),
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Call(
                                        func=Name(id="field_class", ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                value=Name(
                                                    id="field_kwargs", ctx=Load()
                                                )
                                            )
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="fields", ctx=Load()),
                                    attr="update",
                                    ctx=Load(),
                                ),
                                args=[Name(id="hidden_fields", ctx=Load())],
                                keywords=[],
                            )
                        ),
                        Return(value=Name(id="fields", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_field_names",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="declared_fields"),
                            arg(arg="info"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Returns the list of all field names that should be created when\n        instantiating this serializer class. This is based on the default\n        set of fields, but also takes into account the `Meta.fields` or\n        `Meta.exclude` options if they have been specified.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="fields", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="Meta",
                                        ctx=Load(),
                                    ),
                                    Constant(value="fields"),
                                    Constant(value=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="exclude", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="Meta",
                                        ctx=Load(),
                                    ),
                                    Constant(value="exclude"),
                                    Constant(value=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id="fields", ctx=Load()),
                                    Compare(
                                        left=Name(id="fields", ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Name(id="ALL_FIELDS", ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id="isinstance", ctx=Load()),
                                            args=[
                                                Name(id="fields", ctx=Load()),
                                                Tuple(
                                                    elts=[
                                                        Name(id="list", ctx=Load()),
                                                        Name(id="tuple", ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id="TypeError", ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(
                                                    value='The `fields` option must be a list or tuple or "__all__". Got %s.'
                                                ),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Call(
                                                        func=Name(
                                                            id="type", ctx=Load()
                                                        ),
                                                        args=[
                                                            Name(
                                                                id="fields", ctx=Load()
                                                            )
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr="__name__",
                                                    ctx=Load(),
                                                ),
                                            )
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id="exclude", ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id="isinstance", ctx=Load()),
                                            args=[
                                                Name(id="exclude", ctx=Load()),
                                                Tuple(
                                                    elts=[
                                                        Name(id="list", ctx=Load()),
                                                        Name(id="tuple", ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id="TypeError", ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(
                                                    value="The `exclude` option must be a list or tuple. Got %s."
                                                ),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Call(
                                                        func=Name(
                                                            id="type", ctx=Load()
                                                        ),
                                                        args=[
                                                            Name(
                                                                id="exclude", ctx=Load()
                                                            )
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr="__name__",
                                                    ctx=Load(),
                                                ),
                                            )
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Assert(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Name(id="fields", ctx=Load()),
                                        Name(id="exclude", ctx=Load()),
                                    ],
                                ),
                            ),
                            msg=Call(
                                func=Attribute(
                                    value=Constant(
                                        value="Cannot set both 'fields' and 'exclude' options on serializer {serializer_class}."
                                    ),
                                    attr="format",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg="serializer_class",
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id="self", ctx=Load()),
                                                attr="__class__",
                                                ctx=Load(),
                                            ),
                                            attr="__name__",
                                            ctx=Load(),
                                        ),
                                    )
                                ],
                            ),
                        ),
                        Assert(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Compare(
                                            left=Name(id="fields", ctx=Load()),
                                            ops=[Is()],
                                            comparators=[Constant(value=None)],
                                        ),
                                        Compare(
                                            left=Name(id="exclude", ctx=Load()),
                                            ops=[Is()],
                                            comparators=[Constant(value=None)],
                                        ),
                                    ],
                                ),
                            ),
                            msg=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(
                                                value="Creating a ModelSerializer without either the 'fields' attribute or the 'exclude' attribute has been deprecated since 3.3.0, and is now disallowed. Add an explicit fields = '__all__' to the {serializer_class} serializer."
                                            ),
                                            attr="format",
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg="serializer_class",
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(
                                                            id="self", ctx=Load()
                                                        ),
                                                        attr="__class__",
                                                        ctx=Load(),
                                                    ),
                                                    attr="__name__",
                                                    ctx=Load(),
                                                ),
                                            )
                                        ],
                                    )
                                ],
                                ctx=Load(),
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id="fields", ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id="ALL_FIELDS", ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="fields", ctx=Store())],
                                    value=Constant(value=None),
                                )
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id="fields", ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id="required_field_names", ctx=Store())
                                    ],
                                    value=Call(
                                        func=Name(id="set", ctx=Load()),
                                        args=[Name(id="declared_fields", ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id="cls", ctx=Store()),
                                    iter=Attribute(
                                        value=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="__class__",
                                            ctx=Load(),
                                        ),
                                        attr="__bases__",
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(
                                                id="required_field_names", ctx=Store()
                                            ),
                                            op=Sub(),
                                            value=Call(
                                                func=Name(id="set", ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(
                                                            id="getattr", ctx=Load()
                                                        ),
                                                        args=[
                                                            Name(id="cls", ctx=Load()),
                                                            Constant(
                                                                value="_declared_fields"
                                                            ),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    )
                                                ],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id="field_name", ctx=Store()),
                                    iter=Name(id="required_field_names", ctx=Load()),
                                    body=[
                                        Assert(
                                            test=Compare(
                                                left=Name(id="field_name", ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Name(id="fields", ctx=Load())
                                                ],
                                            ),
                                            msg=Call(
                                                func=Attribute(
                                                    value=Constant(
                                                        value="The field '{field_name}' was declared on serializer {serializer_class}, but has not been included in the 'fields' option."
                                                    ),
                                                    attr="format",
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg="field_name",
                                                        value=Name(
                                                            id="field_name", ctx=Load()
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg="serializer_class",
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(
                                                                    id="self",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="__class__",
                                                                ctx=Load(),
                                                            ),
                                                            attr="__name__",
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        )
                                    ],
                                    orelse=[],
                                ),
                                Return(value=Name(id="fields", ctx=Load())),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="fields", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="get_default_field_names",
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id="declared_fields", ctx=Load()),
                                    Name(id="info", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id="exclude", ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None)],
                            ),
                            body=[
                                For(
                                    target=Name(id="field_name", ctx=Store()),
                                    iter=Name(id="exclude", ctx=Load()),
                                    body=[
                                        Assert(
                                            test=Compare(
                                                left=Name(id="field_name", ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(
                                                            id="self", ctx=Load()
                                                        ),
                                                        attr="_declared_fields",
                                                        ctx=Load(),
                                                    )
                                                ],
                                            ),
                                            msg=Call(
                                                func=Attribute(
                                                    value=Constant(
                                                        value="Cannot both declare the field '{field_name}' and include it in the {serializer_class} 'exclude' option. Remove the field or, if inherited from a parent serializer, disable with `{field_name} = None`."
                                                    ),
                                                    attr="format",
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg="field_name",
                                                        value=Name(
                                                            id="field_name", ctx=Load()
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg="serializer_class",
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(
                                                                    id="self",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="__class__",
                                                                ctx=Load(),
                                                            ),
                                                            attr="__name__",
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Assert(
                                            test=Compare(
                                                left=Name(id="field_name", ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Name(id="fields", ctx=Load())
                                                ],
                                            ),
                                            msg=Call(
                                                func=Attribute(
                                                    value=Constant(
                                                        value="The field '{field_name}' was included on serializer {serializer_class} in the 'exclude' option, but does not match any model field."
                                                    ),
                                                    attr="format",
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg="field_name",
                                                        value=Name(
                                                            id="field_name", ctx=Load()
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg="serializer_class",
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(
                                                                    id="self",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="__class__",
                                                                ctx=Load(),
                                                            ),
                                                            attr="__name__",
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="fields", ctx=Load()),
                                                    attr="remove",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id="field_name", ctx=Load())
                                                ],
                                                keywords=[],
                                            )
                                        ),
                                    ],
                                    orelse=[],
                                )
                            ],
                            orelse=[],
                        ),
                        Return(value=Name(id="fields", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_default_field_names",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="declared_fields"),
                            arg(arg="model_info"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Return the default list of field names that will be used if the\n        `Meta.fields` option is not specified.\n        "
                            )
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=List(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(
                                                            id="model_info", ctx=Load()
                                                        ),
                                                        attr="pk",
                                                        ctx=Load(),
                                                    ),
                                                    attr="name",
                                                    ctx=Load(),
                                                )
                                            ],
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id="list", ctx=Load()),
                                            args=[
                                                Name(id="declared_fields", ctx=Load())
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    op=Add(),
                                    right=Call(
                                        func=Name(id="list", ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id="model_info", ctx=Load()),
                                                attr="fields",
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id="list", ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id="model_info", ctx=Load()),
                                            attr="forward_relations",
                                            ctx=Load(),
                                        )
                                    ],
                                    keywords=[],
                                ),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="build_field",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="field_name"),
                            arg(arg="info"),
                            arg(arg="model_class"),
                            arg(arg="nested_depth"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Return a two tuple of (cls, kwargs) to build a serializer field with.\n        "
                            )
                        ),
                        If(
                            test=Compare(
                                left=Name(id="field_name", ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id="info", ctx=Load()),
                                        attr="fields_and_pk",
                                        ctx=Load(),
                                    )
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="model_field", ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id="info", ctx=Load()),
                                            attr="fields_and_pk",
                                            ctx=Load(),
                                        ),
                                        slice=Name(id="field_name", ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="build_standard_field",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id="field_name", ctx=Load()),
                                            Name(id="model_field", ctx=Load()),
                                        ],
                                        keywords=[],
                                    )
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id="field_name", ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id="info", ctx=Load()),
                                                attr="relations",
                                                ctx=Load(),
                                            )
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id="relation_info", ctx=Store())
                                            ],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id="info", ctx=Load()),
                                                    attr="relations",
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id="field_name", ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(
                                                    id="nested_depth", ctx=Load()
                                                ),
                                            ),
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="build_relational_field",
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(
                                                                id="field_name",
                                                                ctx=Load(),
                                                            ),
                                                            Name(
                                                                id="relation_info",
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    )
                                                )
                                            ],
                                            orelse=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="build_nested_field",
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(
                                                                id="field_name",
                                                                ctx=Load(),
                                                            ),
                                                            Name(
                                                                id="relation_info",
                                                                ctx=Load(),
                                                            ),
                                                            Name(
                                                                id="nested_depth",
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    )
                                                )
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id="hasattr", ctx=Load()),
                                                args=[
                                                    Name(id="model_class", ctx=Load()),
                                                    Name(id="field_name", ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(
                                                                id="self", ctx=Load()
                                                            ),
                                                            attr="build_property_field",
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(
                                                                id="field_name",
                                                                ctx=Load(),
                                                            ),
                                                            Name(
                                                                id="model_class",
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    )
                                                )
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(
                                                            id="field_name", ctx=Load()
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(
                                                                    id="self",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="url_field_name",
                                                                ctx=Load(),
                                                            )
                                                        ],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(
                                                                        id="self",
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr="build_url_field",
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(
                                                                        id="field_name",
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(
                                                                        id="model_class",
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            )
                                                        )
                                                    ],
                                                    orelse=[],
                                                )
                                            ],
                                        )
                                    ],
                                )
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="build_unknown_field",
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id="field_name", ctx=Load()),
                                    Name(id="model_class", ctx=Load()),
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="build_standard_field",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="field_name"),
                            arg(arg="model_field"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Create regular model fields.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="field_mapping", ctx=Store())],
                            value=Call(
                                func=Name(id="ClassLookupDict", ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="serializer_field_mapping",
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="field_class", ctx=Store())],
                            value=Subscript(
                                value=Name(id="field_mapping", ctx=Load()),
                                slice=Name(id="model_field", ctx=Load()),
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id="field_kwargs", ctx=Store())],
                            value=Call(
                                func=Name(id="get_field_kwargs", ctx=Load()),
                                args=[
                                    Name(id="field_name", ctx=Load()),
                                    Name(id="model_field", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id="model_field", ctx=Load()),
                                        attr="one_to_one",
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id="model_field", ctx=Load()),
                                        attr="primary_key",
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="field_class", ctx=Store())],
                                    value=Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="serializer_related_field",
                                        ctx=Load(),
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id="field_kwargs", ctx=Load()),
                                            slice=Constant(value="queryset"),
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id="model_field", ctx=Load()),
                                            attr="related_model",
                                            ctx=Load(),
                                        ),
                                        attr="objects",
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value="choices"),
                                ops=[In()],
                                comparators=[Name(id="field_kwargs", ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="field_class", ctx=Store())],
                                    value=Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="serializer_choice_field",
                                        ctx=Load(),
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id="valid_kwargs", ctx=Store())],
                                    value=Set(
                                        elts=[
                                            Constant(value="read_only"),
                                            Constant(value="write_only"),
                                            Constant(value="required"),
                                            Constant(value="default"),
                                            Constant(value="initial"),
                                            Constant(value="source"),
                                            Constant(value="label"),
                                            Constant(value="help_text"),
                                            Constant(value="style"),
                                            Constant(value="error_messages"),
                                            Constant(value="validators"),
                                            Constant(value="allow_null"),
                                            Constant(value="allow_blank"),
                                            Constant(value="choices"),
                                        ]
                                    ),
                                ),
                                For(
                                    target=Name(id="key", ctx=Store()),
                                    iter=Call(
                                        func=Name(id="list", ctx=Load()),
                                        args=[Name(id="field_kwargs", ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id="key", ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Name(id="valid_kwargs", ctx=Load())
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(
                                                                id="field_kwargs",
                                                                ctx=Load(),
                                                            ),
                                                            attr="pop",
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id="key", ctx=Load())
                                                        ],
                                                        keywords=[],
                                                    )
                                                )
                                            ],
                                            orelse=[],
                                        )
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="issubclass", ctx=Load()),
                                    args=[
                                        Name(id="field_class", ctx=Load()),
                                        Name(id="ModelField", ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="field_kwargs", ctx=Load()),
                                            attr="pop",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="model_field"),
                                            Constant(value=None),
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id="issubclass", ctx=Load()),
                                            args=[
                                                Name(id="field_class", ctx=Load()),
                                                Name(id="CharField", ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id="issubclass", ctx=Load()),
                                            args=[
                                                Name(id="field_class", ctx=Load()),
                                                Name(id="ChoiceField", ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="field_kwargs", ctx=Load()),
                                            attr="pop",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="allow_blank"),
                                            Constant(value=None),
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="is_django_jsonfield", ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id="hasattr", ctx=Load()),
                                        args=[
                                            Name(id="models", ctx=Load()),
                                            Constant(value="JSONField"),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id="isinstance", ctx=Load()),
                                        args=[
                                            Name(id="model_field", ctx=Load()),
                                            Attribute(
                                                value=Name(id="models", ctx=Load()),
                                                attr="JSONField",
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id="postgres_fields", ctx=Load()),
                                            Call(
                                                func=Name(id="isinstance", ctx=Load()),
                                                args=[
                                                    Name(id="model_field", ctx=Load()),
                                                    Attribute(
                                                        value=Name(
                                                            id="postgres_fields",
                                                            ctx=Load(),
                                                        ),
                                                        attr="JSONField",
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Name(id="is_django_jsonfield", ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id="field_kwargs", ctx=Load()),
                                            slice=Constant(value="encoder"),
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Call(
                                        func=Name(id="getattr", ctx=Load()),
                                        args=[
                                            Name(id="model_field", ctx=Load()),
                                            Constant(value="encoder"),
                                            Constant(value=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id="is_django_jsonfield", ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(
                                                        id="field_kwargs", ctx=Load()
                                                    ),
                                                    slice=Constant(value="decoder"),
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=Call(
                                                func=Name(id="getattr", ctx=Load()),
                                                args=[
                                                    Name(id="model_field", ctx=Load()),
                                                    Constant(value="decoder"),
                                                    Constant(value=None),
                                                ],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id="postgres_fields", ctx=Load()),
                                    Call(
                                        func=Name(id="isinstance", ctx=Load()),
                                        args=[
                                            Name(id="model_field", ctx=Load()),
                                            Attribute(
                                                value=Name(
                                                    id="postgres_fields", ctx=Load()
                                                ),
                                                attr="ArrayField",
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id="child_model_field", ctx=Store())],
                                    value=Attribute(
                                        value=Name(id="model_field", ctx=Load()),
                                        attr="base_field",
                                        ctx=Load(),
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(
                                                    id="child_field_class", ctx=Store()
                                                ),
                                                Name(
                                                    id="child_field_kwargs", ctx=Store()
                                                ),
                                            ],
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="build_standard_field",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="child"),
                                            Name(id="child_model_field", ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id="field_kwargs", ctx=Load()),
                                            slice=Constant(value="child"),
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Call(
                                        func=Name(id="child_field_class", ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                value=Name(
                                                    id="child_field_kwargs", ctx=Load()
                                                )
                                            )
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id="field_class", ctx=Load()),
                                    Name(id="field_kwargs", ctx=Load()),
                                ],
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="build_relational_field",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="field_name"),
                            arg(arg="relation_info"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Create fields for forward and reverse relationships.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="field_class", ctx=Store())],
                            value=Attribute(
                                value=Name(id="self", ctx=Load()),
                                attr="serializer_related_field",
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id="field_kwargs", ctx=Store())],
                            value=Call(
                                func=Name(id="get_relation_kwargs", ctx=Load()),
                                args=[
                                    Name(id="field_name", ctx=Load()),
                                    Name(id="relation_info", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="to_field", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="field_kwargs", ctx=Load()),
                                    attr="pop",
                                    ctx=Load(),
                                ),
                                args=[Constant(value="to_field"), Constant(value=None)],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id="to_field", ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id="relation_info", ctx=Load()),
                                            attr="reverse",
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(
                                                                id="relation_info",
                                                                ctx=Load(),
                                                            ),
                                                            attr="related_model",
                                                            ctx=Load(),
                                                        ),
                                                        attr="_meta",
                                                        ctx=Load(),
                                                    ),
                                                    attr="get_field",
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id="to_field", ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr="primary_key",
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id="field_kwargs", ctx=Load()),
                                            slice=Constant(value="slug_field"),
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Name(id="to_field", ctx=Load()),
                                ),
                                Assign(
                                    targets=[Name(id="field_class", ctx=Store())],
                                    value=Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="serializer_related_to_field",
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id="issubclass", ctx=Load()),
                                    args=[
                                        Name(id="field_class", ctx=Load()),
                                        Name(id="HyperlinkedRelatedField", ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="field_kwargs", ctx=Load()),
                                            attr="pop",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="view_name"),
                                            Constant(value=None),
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id="field_class", ctx=Load()),
                                    Name(id="field_kwargs", ctx=Load()),
                                ],
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="build_nested_field",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="field_name"),
                            arg(arg="relation_info"),
                            arg(arg="nested_depth"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Create nested fields for forward and reverse relationships.\n        "
                            )
                        ),
                        ClassDef(
                            name="NestedSerializer",
                            bases=[Name(id="ModelSerializer", ctx=Load())],
                            keywords=[],
                            body=[
                                ClassDef(
                                    name="Meta",
                                    bases=[],
                                    keywords=[],
                                    body=[
                                        Assign(
                                            targets=[Name(id="model", ctx=Store())],
                                            value=Attribute(
                                                value=Name(
                                                    id="relation_info", ctx=Load()
                                                ),
                                                attr="related_model",
                                                ctx=Load(),
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id="depth", ctx=Store())],
                                            value=BinOp(
                                                left=Name(
                                                    id="nested_depth", ctx=Load()
                                                ),
                                                op=Sub(),
                                                right=Constant(value=1),
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id="fields", ctx=Store())],
                                            value=Constant(value="__all__"),
                                        ),
                                    ],
                                    decorator_list=[],
                                )
                            ],
                            decorator_list=[],
                        ),
                        Assign(
                            targets=[Name(id="field_class", ctx=Store())],
                            value=Name(id="NestedSerializer", ctx=Load()),
                        ),
                        Assign(
                            targets=[Name(id="field_kwargs", ctx=Store())],
                            value=Call(
                                func=Name(id="get_nested_relation_kwargs", ctx=Load()),
                                args=[Name(id="relation_info", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id="field_class", ctx=Load()),
                                    Name(id="field_kwargs", ctx=Load()),
                                ],
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="build_property_field",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="field_name"),
                            arg(arg="model_class"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Create a read only field for model methods and properties.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="field_class", ctx=Store())],
                            value=Name(id="ReadOnlyField", ctx=Load()),
                        ),
                        Assign(
                            targets=[Name(id="field_kwargs", ctx=Store())],
                            value=Dict(keys=[], values=[]),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id="field_class", ctx=Load()),
                                    Name(id="field_kwargs", ctx=Load()),
                                ],
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="build_url_field",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="field_name"),
                            arg(arg="model_class"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Create a field representing the object's own URL.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="field_class", ctx=Store())],
                            value=Attribute(
                                value=Name(id="self", ctx=Load()),
                                attr="serializer_url_field",
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id="field_kwargs", ctx=Store())],
                            value=Call(
                                func=Name(id="get_url_kwargs", ctx=Load()),
                                args=[Name(id="model_class", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id="field_class", ctx=Load()),
                                    Name(id="field_kwargs", ctx=Load()),
                                ],
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="build_unknown_field",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="field_name"),
                            arg(arg="model_class"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Raise an error on any unknown fields.\n        "
                            )
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id="ImproperlyConfigured", ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(
                                            value="Field name `%s` is not valid for model `%s`."
                                        ),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id="field_name", ctx=Load()),
                                                Attribute(
                                                    value=Name(
                                                        id="model_class", ctx=Load()
                                                    ),
                                                    attr="__name__",
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="include_extra_kwargs",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="kwargs"),
                            arg(arg="extra_kwargs"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Include any 'extra_kwargs' that have been included for this field,\n        possibly removing any incompatible existing keyword arguments.\n        "
                            )
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id="extra_kwargs", ctx=Load()),
                                    attr="get",
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="read_only"),
                                    Constant(value=False),
                                ],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id="attr", ctx=Store()),
                                    iter=List(
                                        elts=[
                                            Constant(value="required"),
                                            Constant(value="default"),
                                            Constant(value="allow_blank"),
                                            Constant(value="allow_null"),
                                            Constant(value="min_length"),
                                            Constant(value="max_length"),
                                            Constant(value="min_value"),
                                            Constant(value="max_value"),
                                            Constant(value="validators"),
                                            Constant(value="queryset"),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="kwargs", ctx=Load()),
                                                    attr="pop",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id="attr", ctx=Load()),
                                                    Constant(value=None),
                                                ],
                                                keywords=[],
                                            )
                                        )
                                    ],
                                    orelse=[],
                                )
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id="extra_kwargs", ctx=Load()),
                                            attr="get",
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value="default")],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id="kwargs", ctx=Load()),
                                                attr="get",
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value="required")],
                                            keywords=[],
                                        ),
                                        ops=[Is()],
                                        comparators=[Constant(value=False)],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="kwargs", ctx=Load()),
                                            attr="pop",
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value="required")],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id="extra_kwargs", ctx=Load()),
                                    attr="get",
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="read_only"),
                                    Call(
                                        func=Attribute(
                                            value=Name(id="kwargs", ctx=Load()),
                                            attr="get",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="read_only"),
                                            Constant(value=False),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id="extra_kwargs", ctx=Load()),
                                            attr="pop",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="required"),
                                            Constant(value=None),
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="kwargs", ctx=Load()),
                                    attr="update",
                                    ctx=Load(),
                                ),
                                args=[Name(id="extra_kwargs", ctx=Load())],
                                keywords=[],
                            )
                        ),
                        Return(value=Name(id="kwargs", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_extra_kwargs",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Return a dictionary mapping field names to a dictionary of\n        additional keyword arguments.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="extra_kwargs", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="copy", ctx=Load()),
                                    attr="deepcopy",
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id="getattr", ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id="self", ctx=Load()),
                                                attr="Meta",
                                                ctx=Load(),
                                            ),
                                            Constant(value="extra_kwargs"),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    )
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="read_only_fields", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="Meta",
                                        ctx=Load(),
                                    ),
                                    Constant(value="read_only_fields"),
                                    Constant(value=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id="read_only_fields", ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None)],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id="isinstance", ctx=Load()),
                                            args=[
                                                Name(id="read_only_fields", ctx=Load()),
                                                Tuple(
                                                    elts=[
                                                        Name(id="list", ctx=Load()),
                                                        Name(id="tuple", ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id="TypeError", ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(
                                                            value="The `read_only_fields` option must be a list or tuple. Got %s."
                                                        ),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Call(
                                                                func=Name(
                                                                    id="type",
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(
                                                                        id="read_only_fields",
                                                                        ctx=Load(),
                                                                    )
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr="__name__",
                                                            ctx=Load(),
                                                        ),
                                                    )
                                                ],
                                                keywords=[],
                                            )
                                        )
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id="field_name", ctx=Store()),
                                    iter=Name(id="read_only_fields", ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id="kwargs", ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(
                                                        id="extra_kwargs", ctx=Load()
                                                    ),
                                                    attr="get",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id="field_name", ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id="kwargs", ctx=Load()),
                                                    slice=Constant(value="read_only"),
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=Constant(value=True),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(
                                                        id="extra_kwargs", ctx=Load()
                                                    ),
                                                    slice=Name(
                                                        id="field_name", ctx=Load()
                                                    ),
                                                    ctx=Store(),
                                                )
                                            ],
                                            value=Name(id="kwargs", ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assert(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id="hasattr", ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="Meta",
                                                    ctx=Load(),
                                                ),
                                                Constant(value="readonly_fields"),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    msg=BinOp(
                                        left=Constant(
                                            value="Serializer `%s.%s` has field `readonly_fields`; the correct spelling for the option is `read_only_fields`."
                                        ),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(
                                                            id="self", ctx=Load()
                                                        ),
                                                        attr="__class__",
                                                        ctx=Load(),
                                                    ),
                                                    attr="__module__",
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(
                                                            id="self", ctx=Load()
                                                        ),
                                                        attr="__class__",
                                                        ctx=Load(),
                                                    ),
                                                    attr="__name__",
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                )
                            ],
                        ),
                        Return(value=Name(id="extra_kwargs", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_uniqueness_extra_kwargs",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="field_names"),
                            arg(arg="declared_fields"),
                            arg(arg="extra_kwargs"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Return any additional field options that need to be included as a\n        result of uniqueness constraints on the model. This is returned as\n        a two-tuple of:\n\n        ('dict of updated extra kwargs', 'mapping of hidden fields')\n        "
                            )
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id="getattr", ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="Meta",
                                            ctx=Load(),
                                        ),
                                        Constant(value="validators"),
                                        Constant(value=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None)],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id="extra_kwargs", ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        ctx=Load(),
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="model", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="Meta",
                                        ctx=Load(),
                                    ),
                                    Constant(value="model"),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="model_fields", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="self", ctx=Load()),
                                    attr="_get_model_fields",
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id="field_names", ctx=Load()),
                                    Name(id="declared_fields", ctx=Load()),
                                    Name(id="extra_kwargs", ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="unique_constraint_names", ctx=Store())],
                            value=Call(
                                func=Name(id="set", ctx=Load()), args=[], keywords=[]
                            ),
                        ),
                        For(
                            target=Name(id="model_field", ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id="model_fields", ctx=Load()),
                                    attr="values",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(
                                        id="unique_constraint_names", ctx=Store()
                                    ),
                                    op=BitOr(),
                                    value=Set(
                                        elts=[
                                            Attribute(
                                                value=Name(
                                                    id="model_field", ctx=Load()
                                                ),
                                                attr="unique_for_date",
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(
                                                    id="model_field", ctx=Load()
                                                ),
                                                attr="unique_for_month",
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(
                                                    id="model_field", ctx=Load()
                                                ),
                                                attr="unique_for_year",
                                                ctx=Load(),
                                            ),
                                        ]
                                    ),
                                )
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Name(id="unique_constraint_names", ctx=Store()),
                            op=Sub(),
                            value=Set(elts=[Constant(value=None)]),
                        ),
                        For(
                            target=Name(id="parent_class", ctx=Store()),
                            iter=BinOp(
                                left=List(
                                    elts=[Name(id="model", ctx=Load())], ctx=Load()
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id="list", ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id="model", ctx=Load()),
                                                attr="_meta",
                                                ctx=Load(),
                                            ),
                                            attr="parents",
                                            ctx=Load(),
                                        )
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                For(
                                    target=Name(id="unique_together_list", ctx=Store()),
                                    iter=Attribute(
                                        value=Attribute(
                                            value=Name(id="parent_class", ctx=Load()),
                                            attr="_meta",
                                            ctx=Load(),
                                        ),
                                        attr="unique_together",
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id="set", ctx=Load()),
                                                        args=[
                                                            Name(
                                                                id="field_names",
                                                                ctx=Load(),
                                                            )
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr="issuperset",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(
                                                        id="unique_together_list",
                                                        ctx=Load(),
                                                    )
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(
                                                        id="unique_constraint_names",
                                                        ctx=Store(),
                                                    ),
                                                    op=BitOr(),
                                                    value=Call(
                                                        func=Name(id="set", ctx=Load()),
                                                        args=[
                                                            Name(
                                                                id="unique_together_list",
                                                                ctx=Load(),
                                                            )
                                                        ],
                                                        keywords=[],
                                                    ),
                                                )
                                            ],
                                            orelse=[],
                                        )
                                    ],
                                    orelse=[],
                                )
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="hidden_fields", ctx=Store())],
                            value=Dict(keys=[], values=[]),
                        ),
                        Assign(
                            targets=[Name(id="uniqueness_extra_kwargs", ctx=Store())],
                            value=Dict(keys=[], values=[]),
                        ),
                        For(
                            target=Name(id="unique_constraint_name", ctx=Store()),
                            iter=Name(id="unique_constraint_names", ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id="unique_constraint_field", ctx=Store())
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id="model", ctx=Load()),
                                                attr="_meta",
                                                ctx=Load(),
                                            ),
                                            attr="get_field",
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(
                                                id="unique_constraint_name", ctx=Load()
                                            )
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Call(
                                        func=Name(id="getattr", ctx=Load()),
                                        args=[
                                            Name(
                                                id="unique_constraint_field", ctx=Load()
                                            ),
                                            Constant(value="auto_now_add"),
                                            Constant(value=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id="default", ctx=Store())],
                                            value=Call(
                                                func=Name(
                                                    id="CreateOnlyDefault", ctx=Load()
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(
                                                            id="timezone", ctx=Load()
                                                        ),
                                                        attr="now",
                                                        ctx=Load(),
                                                    )
                                                ],
                                                keywords=[],
                                            ),
                                        )
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id="getattr", ctx=Load()),
                                                args=[
                                                    Name(
                                                        id="unique_constraint_field",
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value="auto_now"),
                                                    Constant(value=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Name(id="default", ctx=Store())
                                                    ],
                                                    value=Attribute(
                                                        value=Name(
                                                            id="timezone", ctx=Load()
                                                        ),
                                                        attr="now",
                                                        ctx=Load(),
                                                    ),
                                                )
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(
                                                                id="unique_constraint_field",
                                                                ctx=Load(),
                                                            ),
                                                            attr="has_default",
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Name(
                                                                    id="default",
                                                                    ctx=Store(),
                                                                )
                                                            ],
                                                            value=Attribute(
                                                                value=Name(
                                                                    id="unique_constraint_field",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="default",
                                                                ctx=Load(),
                                                            ),
                                                        )
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Name(
                                                                    id="default",
                                                                    ctx=Store(),
                                                                )
                                                            ],
                                                            value=Name(
                                                                id="empty", ctx=Load()
                                                            ),
                                                        )
                                                    ],
                                                )
                                            ],
                                        )
                                    ],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(
                                            id="unique_constraint_name", ctx=Load()
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Name(id="model_fields", ctx=Load())
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id="default", ctx=Load()),
                                                ops=[Is()],
                                                comparators=[
                                                    Name(id="empty", ctx=Load())
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(
                                                                id="uniqueness_extra_kwargs",
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(
                                                                id="unique_constraint_name",
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value="required")
                                                        ],
                                                        values=[Constant(value=True)],
                                                    ),
                                                )
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(
                                                                id="uniqueness_extra_kwargs",
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(
                                                                id="unique_constraint_name",
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value="default")
                                                        ],
                                                        values=[
                                                            Name(
                                                                id="default", ctx=Load()
                                                            )
                                                        ],
                                                    ),
                                                )
                                            ],
                                        )
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id="default", ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[
                                                    Name(id="empty", ctx=Load())
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(
                                                                id="hidden_fields",
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(
                                                                id="unique_constraint_name",
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Call(
                                                        func=Name(
                                                            id="HiddenField", ctx=Load()
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg="default",
                                                                value=Name(
                                                                    id="default",
                                                                    ctx=Load(),
                                                                ),
                                                            )
                                                        ],
                                                    ),
                                                )
                                            ],
                                            orelse=[],
                                        )
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id="key", ctx=Store()),
                                    Name(id="value", ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(
                                        id="uniqueness_extra_kwargs", ctx=Load()
                                    ),
                                    attr="items",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id="key", ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Name(id="extra_kwargs", ctx=Load())
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id="value", ctx=Load()),
                                                    attr="update",
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(
                                                            id="extra_kwargs",
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(
                                                            id="key", ctx=Load()
                                                        ),
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
                                    targets=[
                                        Subscript(
                                            value=Name(id="extra_kwargs", ctx=Load()),
                                            slice=Name(id="key", ctx=Load()),
                                            ctx=Store(),
                                        )
                                    ],
                                    value=Name(id="value", ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id="extra_kwargs", ctx=Load()),
                                    Name(id="hidden_fields", ctx=Load()),
                                ],
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="_get_model_fields",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="field_names"),
                            arg(arg="declared_fields"),
                            arg(arg="extra_kwargs"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Returns all the model fields that are being mapped to by fields\n        on the serializer class.\n        Returned as a dict of 'model field name' -> 'model field'.\n        Used internally by `get_uniqueness_field_options`.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="model", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="Meta",
                                        ctx=Load(),
                                    ),
                                    Constant(value="model"),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="model_fields", ctx=Store())],
                            value=Dict(keys=[], values=[]),
                        ),
                        For(
                            target=Name(id="field_name", ctx=Store()),
                            iter=Name(id="field_names", ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id="field_name", ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Name(id="declared_fields", ctx=Load())
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id="field", ctx=Store())],
                                            value=Subscript(
                                                value=Name(
                                                    id="declared_fields", ctx=Load()
                                                ),
                                                slice=Name(id="field_name", ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id="source", ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(
                                                            id="field", ctx=Load()
                                                        ),
                                                        attr="source",
                                                        ctx=Load(),
                                                    ),
                                                    Name(id="field_name", ctx=Load()),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Name(id="source", ctx=Store())
                                                    ],
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(
                                                                id="extra_kwargs",
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(
                                                                id="field_name",
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value="source"),
                                                        ctx=Load(),
                                                    ),
                                                )
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(
                                                        id="KeyError", ctx=Load()
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Name(
                                                                    id="source",
                                                                    ctx=Store(),
                                                                )
                                                            ],
                                                            value=Name(
                                                                id="field_name",
                                                                ctx=Load(),
                                                            ),
                                                        )
                                                    ],
                                                )
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        )
                                    ],
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Constant(value="."),
                                                ops=[In()],
                                                comparators=[
                                                    Name(id="source", ctx=Load())
                                                ],
                                            ),
                                            Compare(
                                                left=Name(id="source", ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value="*")],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id="field", ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(
                                                            id="model", ctx=Load()
                                                        ),
                                                        attr="_meta",
                                                        ctx=Load(),
                                                    ),
                                                    attr="get_field",
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id="source", ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id="isinstance", ctx=Load()),
                                                args=[
                                                    Name(id="field", ctx=Load()),
                                                    Name(
                                                        id="DjangoModelField",
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(
                                                                id="model_fields",
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(
                                                                id="source", ctx=Load()
                                                            ),
                                                            ctx=Store(),
                                                        )
                                                    ],
                                                    value=Name(id="field", ctx=Load()),
                                                )
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(
                                                id="FieldDoesNotExist", ctx=Load()
                                            ),
                                            body=[Pass()],
                                        )
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(value=Name(id="model_fields", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_validators",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Determine the set of validators to use when instantiating serializer.\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="validators", ctx=Store())],
                            value=Call(
                                func=Name(id="getattr", ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id="getattr", ctx=Load()),
                                        args=[
                                            Name(id="self", ctx=Load()),
                                            Constant(value="Meta"),
                                            Constant(value=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value="validators"),
                                    Constant(value=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id="validators", ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id="list", ctx=Load()),
                                        args=[Name(id="validators", ctx=Load())],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="get_unique_together_validators",
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="get_unique_for_date_validators",
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_unique_together_validators",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Determine a default set of validators for any unique_together constraints.\n        "
                            )
                        ),
                        Assign(
                            targets=[
                                Name(id="model_class_inheritance_tree", ctx=Store())
                            ],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id="self", ctx=Load()),
                                                attr="Meta",
                                                ctx=Load(),
                                            ),
                                            attr="model",
                                            ctx=Load(),
                                        )
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id="list", ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(
                                                            id="self", ctx=Load()
                                                        ),
                                                        attr="Meta",
                                                        ctx=Load(),
                                                    ),
                                                    attr="model",
                                                    ctx=Load(),
                                                ),
                                                attr="_meta",
                                                ctx=Load(),
                                            ),
                                            attr="parents",
                                            ctx=Load(),
                                        )
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ),
                        Assign(
                            targets=[Name(id="field_sources", ctx=Store())],
                            value=Call(
                                func=Name(id="OrderedDict", ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id="field", ctx=Load()),
                                                    attr="field_name",
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id="field", ctx=Load()),
                                                    attr="source",
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id="field", ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="_writable_fields",
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(
                                                                        id="field",
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr="source",
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[
                                                                    Constant(value="*")
                                                                ],
                                                            ),
                                                            Compare(
                                                                left=Constant(
                                                                    value="."
                                                                ),
                                                                ops=[NotIn()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(
                                                                            id="field",
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr="source",
                                                                        ctx=Load(),
                                                                    )
                                                                ],
                                                            ),
                                                        ],
                                                    )
                                                ],
                                                is_async=0,
                                            )
                                        ],
                                    )
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id="field_sources", ctx=Load()),
                                    attr="update",
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id="OrderedDict", ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(
                                                                id="field", ctx=Load()
                                                            ),
                                                            attr="field_name",
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(
                                                                id="field", ctx=Load()
                                                            ),
                                                            attr="source",
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(
                                                            id="field", ctx=Store()
                                                        ),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(
                                                                        id="self",
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr="fields",
                                                                    ctx=Load(),
                                                                ),
                                                                attr="values",
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(
                                                                            id="field",
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr="read_only",
                                                                        ctx=Load(),
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(
                                                                                id="field",
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr="default",
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[NotEq()],
                                                                        comparators=[
                                                                            Name(
                                                                                id="empty",
                                                                                ctx=Load(),
                                                                            )
                                                                        ],
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(
                                                                                id="field",
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr="source",
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[NotEq()],
                                                                        comparators=[
                                                                            Constant(
                                                                                value="*"
                                                                            )
                                                                        ],
                                                                    ),
                                                                    Compare(
                                                                        left=Constant(
                                                                            value="."
                                                                        ),
                                                                        ops=[NotIn()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(
                                                                                    id="field",
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr="source",
                                                                                ctx=Load(),
                                                                            )
                                                                        ],
                                                                    ),
                                                                ],
                                                            )
                                                        ],
                                                        is_async=0,
                                                    )
                                                ],
                                            )
                                        ],
                                        keywords=[],
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Assign(
                            targets=[Name(id="source_map", ctx=Store())],
                            value=Call(
                                func=Name(id="defaultdict", ctx=Load()),
                                args=[Name(id="list", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id="name", ctx=Store()),
                                    Name(id="source", ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id="field_sources", ctx=Load()),
                                    attr="items",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id="source_map", ctx=Load()),
                                                slice=Name(id="source", ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr="append",
                                            ctx=Load(),
                                        ),
                                        args=[Name(id="name", ctx=Load())],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id="validators", ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                        ),
                        For(
                            target=Name(id="parent_class", ctx=Store()),
                            iter=Name(id="model_class_inheritance_tree", ctx=Load()),
                            body=[
                                For(
                                    target=Name(id="unique_together", ctx=Store()),
                                    iter=Attribute(
                                        value=Attribute(
                                            value=Name(id="parent_class", ctx=Load()),
                                            attr="_meta",
                                            ctx=Load(),
                                        ),
                                        attr="unique_together",
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Name(
                                                                id="set", ctx=Load()
                                                            ),
                                                            args=[
                                                                Name(
                                                                    id="source_map",
                                                                    ctx=Load(),
                                                                )
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr="issuperset",
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(
                                                            id="unique_together",
                                                            ctx=Load(),
                                                        )
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        For(
                                            target=Name(id="source", ctx=Store()),
                                            iter=Name(id="unique_together", ctx=Load()),
                                            body=[
                                                Assert(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(
                                                                id="len", ctx=Load()
                                                            ),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(
                                                                        id="source_map",
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Name(
                                                                        id="source",
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                )
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=1)],
                                                    ),
                                                    msg=Call(
                                                        func=Attribute(
                                                            value=Constant(
                                                                value="Unable to create `UniqueTogetherValidator` for `{model}.{field}` as `{serializer}` has multiple fields ({fields}) that map to this model field. Either remove the extra fields, or override `Meta.validators` with a `UniqueTogetherValidator` using the desired field names."
                                                            ),
                                                            attr="format",
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg="model",
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(
                                                                                id="self",
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr="Meta",
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr="model",
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr="__name__",
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg="serializer",
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(
                                                                            id="self",
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr="__class__",
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr="__name__",
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg="field",
                                                                value=Name(
                                                                    id="source",
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg="fields",
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Constant(
                                                                            value=", "
                                                                        ),
                                                                        attr="join",
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(
                                                                                id="source_map",
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Name(
                                                                                id="source",
                                                                                ctx=Load(),
                                                                            ),
                                                                            ctx=Load(),
                                                                        )
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                )
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Name(id="field_names", ctx=Store())
                                            ],
                                            value=Call(
                                                func=Name(id="tuple", ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Subscript(
                                                            value=Subscript(
                                                                value=Name(
                                                                    id="source_map",
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(
                                                                    id="f", ctx=Load()
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0),
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(
                                                                    id="f", ctx=Store()
                                                                ),
                                                                iter=Name(
                                                                    id="unique_together",
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            )
                                                        ],
                                                    )
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id="validator", ctx=Store())],
                                            value=Call(
                                                func=Name(
                                                    id="UniqueTogetherValidator",
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg="queryset",
                                                        value=Attribute(
                                                            value=Name(
                                                                id="parent_class",
                                                                ctx=Load(),
                                                            ),
                                                            attr="_default_manager",
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg="fields",
                                                        value=Name(
                                                            id="field_names", ctx=Load()
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(
                                                        id="validators", ctx=Load()
                                                    ),
                                                    attr="append",
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id="validator", ctx=Load())],
                                                keywords=[],
                                            )
                                        ),
                                    ],
                                    orelse=[],
                                )
                            ],
                            orelse=[],
                        ),
                        Return(value=Name(id="validators", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="get_unique_for_date_validators",
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg="self")],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Determine a default set of validators for the following constraints:\n\n        * unique_for_date\n        * unique_for_month\n        * unique_for_year\n        "
                            )
                        ),
                        Assign(
                            targets=[Name(id="info", ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id="model_meta", ctx=Load()),
                                    attr="get_field_info",
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id="self", ctx=Load()),
                                            attr="Meta",
                                            ctx=Load(),
                                        ),
                                        attr="model",
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="default_manager", ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id="self", ctx=Load()),
                                        attr="Meta",
                                        ctx=Load(),
                                    ),
                                    attr="model",
                                    ctx=Load(),
                                ),
                                attr="_default_manager",
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id="field_names", ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id="field", ctx=Load()),
                                    attr="source",
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id="field", ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="fields",
                                                    ctx=Load(),
                                                ),
                                                attr="values",
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    )
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id="validators", ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id="field_name", ctx=Store()),
                                    Name(id="field", ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id="info", ctx=Load()),
                                        attr="fields_and_pk",
                                        ctx=Load(),
                                    ),
                                    attr="items",
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id="field", ctx=Load()),
                                                attr="unique_for_date",
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Name(id="field_name", ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Name(id="field_names", ctx=Load())
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id="validator", ctx=Store())],
                                            value=Call(
                                                func=Name(
                                                    id="UniqueForDateValidator",
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg="queryset",
                                                        value=Name(
                                                            id="default_manager",
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg="field",
                                                        value=Name(
                                                            id="field_name", ctx=Load()
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg="date_field",
                                                        value=Attribute(
                                                            value=Name(
                                                                id="field", ctx=Load()
                                                            ),
                                                            attr="unique_for_date",
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(
                                                        id="validators", ctx=Load()
                                                    ),
                                                    attr="append",
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id="validator", ctx=Load())],
                                                keywords=[],
                                            )
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id="field", ctx=Load()),
                                                attr="unique_for_month",
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Name(id="field_name", ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Name(id="field_names", ctx=Load())
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id="validator", ctx=Store())],
                                            value=Call(
                                                func=Name(
                                                    id="UniqueForMonthValidator",
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg="queryset",
                                                        value=Name(
                                                            id="default_manager",
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg="field",
                                                        value=Name(
                                                            id="field_name", ctx=Load()
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg="date_field",
                                                        value=Attribute(
                                                            value=Name(
                                                                id="field", ctx=Load()
                                                            ),
                                                            attr="unique_for_month",
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(
                                                        id="validators", ctx=Load()
                                                    ),
                                                    attr="append",
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id="validator", ctx=Load())],
                                                keywords=[],
                                            )
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id="field", ctx=Load()),
                                                attr="unique_for_year",
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Name(id="field_name", ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Name(id="field_names", ctx=Load())
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id="validator", ctx=Store())],
                                            value=Call(
                                                func=Name(
                                                    id="UniqueForYearValidator",
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg="queryset",
                                                        value=Name(
                                                            id="default_manager",
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg="field",
                                                        value=Name(
                                                            id="field_name", ctx=Load()
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg="date_field",
                                                        value=Attribute(
                                                            value=Name(
                                                                id="field", ctx=Load()
                                                            ),
                                                            attr="unique_for_year",
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(
                                                        id="validators", ctx=Load()
                                                    ),
                                                    attr="append",
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id="validator", ctx=Load())],
                                                keywords=[],
                                            )
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(value=Name(id="validators", ctx=Load())),
                    ],
                    decorator_list=[],
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name="HyperlinkedModelSerializer",
            bases=[Name(id="ModelSerializer", ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(
                        value="\n    A type of `ModelSerializer` that uses hyperlinked relationships instead\n    of primary key relationships. Specifically:\n\n    * A 'url' field is included instead of the 'id' field.\n    * Relationships to other instances are hyperlinks, instead of primary keys.\n    "
                    )
                ),
                Assign(
                    targets=[Name(id="serializer_related_field", ctx=Store())],
                    value=Name(id="HyperlinkedRelatedField", ctx=Load()),
                ),
                FunctionDef(
                    name="get_default_field_names",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="declared_fields"),
                            arg(arg="model_info"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Return the default list of field names that will be used if the\n        `Meta.fields` option is not specified.\n        "
                            )
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=List(
                                            elts=[
                                                Attribute(
                                                    value=Name(id="self", ctx=Load()),
                                                    attr="url_field_name",
                                                    ctx=Load(),
                                                )
                                            ],
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id="list", ctx=Load()),
                                            args=[
                                                Name(id="declared_fields", ctx=Load())
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    op=Add(),
                                    right=Call(
                                        func=Name(id="list", ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id="model_info", ctx=Load()),
                                                attr="fields",
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id="list", ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id="model_info", ctx=Load()),
                                            attr="forward_relations",
                                            ctx=Load(),
                                        )
                                    ],
                                    keywords=[],
                                ),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name="build_nested_field",
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg="self"),
                            arg(arg="field_name"),
                            arg(arg="relation_info"),
                            arg(arg="nested_depth"),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(
                                value="\n        Create nested fields for forward and reverse relationships.\n        "
                            )
                        ),
                        ClassDef(
                            name="NestedSerializer",
                            bases=[Name(id="HyperlinkedModelSerializer", ctx=Load())],
                            keywords=[],
                            body=[
                                ClassDef(
                                    name="Meta",
                                    bases=[],
                                    keywords=[],
                                    body=[
                                        Assign(
                                            targets=[Name(id="model", ctx=Store())],
                                            value=Attribute(
                                                value=Name(
                                                    id="relation_info", ctx=Load()
                                                ),
                                                attr="related_model",
                                                ctx=Load(),
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id="depth", ctx=Store())],
                                            value=BinOp(
                                                left=Name(
                                                    id="nested_depth", ctx=Load()
                                                ),
                                                op=Sub(),
                                                right=Constant(value=1),
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id="fields", ctx=Store())],
                                            value=Constant(value="__all__"),
                                        ),
                                    ],
                                    decorator_list=[],
                                )
                            ],
                            decorator_list=[],
                        ),
                        Assign(
                            targets=[Name(id="field_class", ctx=Store())],
                            value=Name(id="NestedSerializer", ctx=Load()),
                        ),
                        Assign(
                            targets=[Name(id="field_kwargs", ctx=Store())],
                            value=Call(
                                func=Name(id="get_nested_relation_kwargs", ctx=Load()),
                                args=[Name(id="relation_info", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id="field_class", ctx=Load()),
                                    Name(id="field_kwargs", ctx=Load()),
                                ],
                                ctx=Load(),
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
