import argparse
from yapsy.PluginManager import PluginManager


def main():
    parser = argparse.ArgumentParser(description='Validates file format')
    parser.add_argument('files', nargs='+',
                        help='files to be validated')
    parser.add_argument('--verbose', action='store_true',
                        default=False,
                        help='Shows help about validation')

    args = parser.parse_args()

    simplePluginManager = PluginManager()
    simplePluginManager.setPluginPlaces(["plugins"])
    simplePluginManager.collectPlugins()

    for filename in args.files:
        supported = False
        for plugin in simplePluginManager.getAllPlugins():
            methods = plugin.plugin_object
            if methods.should_manage(filename):
                supported = True
                try:
                    plugin.plugin_object.validate(filename)
                    print('%s sintax ok for %s' % (filename, plugin.name))
                    break
                except Exception as e:
                    print('Invalid file %s for %s' % (filename, plugin.name))
                    if args.verbose:
                        print(e)
        if not supported:
            print('%s cannot be validated' % filename)

if __name__ == '__main__':
    main()
