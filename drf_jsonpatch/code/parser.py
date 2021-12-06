import_jsonpatch = """
import jsonpatch
"""


# from rest_framework.parsers import JSONParser
# from rest_framework.exceptions import ParseError

class_JSONPatchParser = '''
class JSONPatchParser(JSONParser):
    """
    Parses PATCH RFC 6902 JSON-serialized data.
    """

    media_type = "application/json-patch+json"

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as JSON and returns the resulting data as json patch.
        """
        data = super().parse(stream, media_type, parser_context)

        try:
            return jsonpatch.JsonPatch(data)
        except jsonpatch.InvalidJsonPatch as exc:
            raise ParseError("JSON Patch (rfc 6902) invalid - %s" % str(exc))
'''
