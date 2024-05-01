from argparse import ArgumentParser
import importlib.metadata

from ephemerality.scripts import init_cmd_parser, init_api_argparse

PROG = "python3 -m ephemerality"


def init_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog=PROG,
        usage="%(prog)s [-h] [-v] {cmd,api} ...",
        description="Runs ephemerality computation module in one of the available mode."
    )
    parser.add_argument(
        "--version", action="version",
        version=f'ephemerality {importlib.metadata.version("ephemerality")}'
    )

    subparsers = parser.add_subparsers(
        prog=PROG,
        help="Use \"cmd\" to run the module once from a command line.\n"
             "Use \"api\" to start a REST web service offering ephemerality computation on request."
    )
    cmd_parser = subparsers.add_parser("cmd")
    api_parser = subparsers.add_parser("api")

    init_cmd_parser(cmd_parser)
    init_api_argparse(api_parser)

    return parser


parser = init_parser()
args = parser.parse_args()
args.func(args)
