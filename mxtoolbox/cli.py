# __main__.py
from .client import MXToolBoxClient, valid_commands
import argparse
from pprint import pprint
import sys

def cli():
    parser = argparse.ArgumentParser(
        prog = 'mxtoolbox',
        description = 'Query the MX ToolBox API and display results.',
        epilog = 'Copyright (c) 2023, Rajesh P. Deo')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--domain-names', nargs='+',
                        help='Domain name to lookup information on.')
    group.add_argument('-l', '--list-commands', action='store_true',
                        help='List available commands for the MX ToolBox API')
    parser.add_argument('-k', '--api_key',
                        help='MX ToolBox API Key, find it in the API section of your user profile.')
    parser.add_argument('-c', '--commands', nargs='+', default=['mx'],
                        help='MX ToolBox API command, use -l to list available commands.')

    args = parser.parse_args()

    if args.list_commands:
        for k, v in valid_commands.items():
            print(f"{k:>10s}: {v:s}")
        return

    mx_client = None

    if args.api_key:
        mx_client = MXToolBoxClient(api_key=args.api_key)

    if mx_client and args.commands and args.domain_names:
        for domain_name in args.domain_names:
            for cmd in args.commands:
                result = mx_client.lookup(domain_name, cmd)
                if result:
                    pprint(result)
                else:
                    continue
    else:
        parser.print_help()

if __name__ == '__main__':
    sys.exit(cli())
