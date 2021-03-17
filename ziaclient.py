from sys import argv

from arguments.parser import create_parser
from client.session import ZIAConnector
from client.utils import print_json, save_json


def main():
    parser = create_parser()
    if len(argv) == 1:
        parser.parse_args(['-h'])

    # Parse args
    args = parser.parse_args()

    client = ZIAConnector(args.conf, not args.no_verbosity)
    client.login()

    result = args.func(client, args)

    save_json(result, args.output)

    if not args.no_print:
        print_json(result)

    if args.apply:
        client.activate_changes()
    if args.pending:
        client.get_status()

    client.logout()


if __name__ == "__main__":
    main()
