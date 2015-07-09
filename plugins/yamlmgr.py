from yapsy.IPlugin import IPlugin
import yaml

class Yaml(IPlugin):
    def should_manage(self, filename):
        lower = filename.lower()
        return lower.endswith('.yaml') or lower.endswith('.yml')

    def validate(self, filename):
        with file(filename) as fd:
            yaml.load(fd)
