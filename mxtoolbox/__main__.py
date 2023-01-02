# __main__.py
from .client import MXToolBoxClient
import argparse
from pprint import pprint
import sys

def main():
    parser = argparse.ArgumentParser(
        prog = 'MX ToolBox Client',
        description = 'Query the MX ToolBox API and display results.',
        epilog = 'Copyright 2023 Rajesh P. Deo <rajesh.deo@gmail.com>')

    parser.add_argument('domain_name')
    parser.add_argument('-k', '--api_key')
    parser.add_argument('-c', '--command')

    args = parser.parse_args()
    print(args.api_key,
          args.command,
          args.domain_name)

    mx_client = None

    if args.api_key:
        mx_client = MXToolBoxClient(api_key=args.api_key)
    else:
        mx_client = MXToolBoxClient()

    if args.command and args.domain_name:
        result = mx_client.lookup(args.domain_name, args.command)
        if result:
            pprint(result)
        else:
            parser.print_usage()

if __name__ == '__main__':
    sys.exit(main())
