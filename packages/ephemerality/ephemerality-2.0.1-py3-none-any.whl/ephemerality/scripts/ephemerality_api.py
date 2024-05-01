import argparse
from argparse import ArgumentParser, Namespace
from subprocess import call


def init_api_argparse(parser: ArgumentParser) -> ArgumentParser:
    parser.usage = "%(prog)s [-h] [--host HOST] [--port PORT] ..."
    parser.description = ("Start a REST web service to compute ephemerality computations on requests. Any additional "
                          "arguments will be passed to the uvicorn service initialisation call.")
    parser.add_argument(
        "--host", action="store", default="127.0.0.1",
        help="Bind socket to this host. Defaults to \"127.0.0.1\"."
    )
    parser.add_argument(
        "--port", action="store", type=int, default=8080,
        help="Bind to a socket with this port. Defaults to 8080."
    )
    parser.add_argument(
        "uvicorn_args", nargs=argparse.REMAINDER,
        help="Arguments to be passed to uvicorn."
    )
    parser.set_defaults(
        func=exec_start_service_call
    )
    return parser


def start_service(host: str = "127.0.0.1", port: int = 8080, uvicorn_args: list | None = None) -> None:
    call_cmd = ['uvicorn', 'ephemerality.rest.runner:app', '--host', host, '--port', str(port)]
    if uvicorn_args:
        call_cmd.extend(uvicorn_args)
    call(call_cmd)


def exec_start_service_call(input_args: Namespace) -> None:
    start_service(host=input_args.host, port=input_args.port, uvicorn_args=input_args.uvicorn_args)
