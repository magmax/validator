from yapsy.IPlugin import IPlugin
import json


class Json(IPlugin):
    def should_manage(self, filename):
        return filename.lower().endswith('.json')

    def validate(self, filename):
        with file(filename) as fd:
            json.load(fd)
