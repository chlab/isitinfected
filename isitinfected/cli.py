"""
isitinfected

Usage:
  isitinfected collect_images
  isitinfected -h | --help
  isitinfected --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  isitinfected collect_images

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/chlab/isitinfected/issues
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import isitinfected.commands
    options = docopt(__doc__, version=VERSION)
    print options
    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items(): 
        if hasattr(isitinfected.commands, k) and v:
            module = getattr(isitinfected.commands, k)
            isitinfected.commands = getmembers(module, isclass)
            command = [command[1] for command in isitinfected.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
