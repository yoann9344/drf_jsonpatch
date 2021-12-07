# Json Patch (RFC 6902) for django rest framework

This implementation hardly depend on [jsonpatch](https://github.com/stefankoegl/python-json-patch), so you should give
a look right there !

## Installation
```python
pip install drf-jsonpatch
```

Then configure your app's settings :
```python
INSTALLED_APPS = [
    ...
    "drf_jsonpatch",
    # Obviously don't forget drf
    "rest_framework",
]

# Then you need to add the new parser to handle the content's type "application/json-patch+json"
# see `drf_jsonpatch.code.parser` and `drf_jsonpatch.patchs.parser`
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.JSONPatchParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
}

```


## Concept
Cause drf is already [full](https://github.com/encode/django-rest-framework/pull/8274) of functionalities, I had to patch it.
