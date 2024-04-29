"""
File: cli.py
-----------------------

A command-line interface (CLI) for interacting with the File Sharing Flask application.

Functions:
    - client_session_manager(host: str, username: str, password: str) -> Generator[FileSharingClient, None, None]:
        Context manager for managing the client session.
    - handle_login(*args, **kwargs): Handle login command.
    - handle_logout(*args, **kwargs): Handle logout command.
    - handle_list(args, file_sharing_client: FileSharingClient): Handle list command.
    - handle_upload(args, file_sharing_client: FileSharingClient): Handle upload command.
    - handle_download(args, file_sharing_client: FileSharingClient): Handle download command.
    - handle_downloadl(args, file_sharing_client: FileSharingClient): Handle downloadl command.
    - build_cli_parser(parser): Build CLI parser.
    - parse_args(): Parse CLI arguments.
    - main(args): Main function to execute CLI commands.

Usage:
    python cli.py <cli_command> [-H HOST] [-u USERNAME] [-p PASSWORD] [-f FILE] [-o OUTPUT] [-n NBFILES] [-r ORDER]

Arguments:
    cli_command : str
        Command to execute (login, logout, list, upload, download, downloadl).
    -H, --host : str, optional
        Host server URL. Default is http://localhost:5000.
    -u, --username : str, optional
        Username for authentication.
    -p, --password : str, optional
        Password for authentication.
    -f, --file : str, optional
        File to upload or download.
    -o, --output : str, optional
        Directory or file path to save the downloaded file.
    -n, --nbfiles : int, optional
        Number of files to list or download.
    -r, --order : str, optional
        Order of files to list or download (asc or desc).

Example:
    python cli.py list -u myusername -p mypassword -n 5
"""

import argparse
from contextlib import contextmanager
from pathlib import Path
from typing import Generator

from flask_file_share.client import FileSharingClient

DEFAULT_BASE_URL = "http://localhost:5000"


@contextmanager
def client_session_manager(host: str, username: str,
                           password: str) -> Generator[FileSharingClient, None, None]:
    """
    Context manager for managing the client session.

    Parameters
    ----------
    host : str
        The host server URL.
    username : str
        The username for authentication.
    password : str
        The password for authentication.

    Yields
    ------
    FileSharingClient
        An instance of the FileSharingClient.

    """
    client = FileSharingClient(username=username, password=password, base_url=host)
    # create a session
    client.login()
    try:
        yield client
    finally:
        # logout even if exception occurs in the block
        client.logout()


def handle_login(args, file_sharing_client: FileSharingClient):  # pylint: disable=W0613
    """
    Handle login command.
    """
    return


def handle_logout(args, file_sharing_client: FileSharingClient):  # pylint: disable=W0613
    """
    Handle logout command.
    """
    return


def handle_list(args, file_sharing_client: FileSharingClient):
    """
    Handle list command.

    Parameters
    ----------
    args : argparse.Namespace
        The parsed command-line arguments.
    file_sharing_client : FileSharingClient
        An instance of the FileSharingClient.

    """
    nb_files = args.nbfiles if args.nbfiles else 10
    order = args.order if args.order else "desc"
    file_sharing_client.list_files(nb_files=nb_files, order=order)


def handle_upload(args, file_sharing_client: FileSharingClient):
    """
    Handle upload command.

    Parameters
    ----------
    args : argparse.Namespace
        The parsed command-line arguments.
    file_sharing_client : FileSharingClient
        An instance of the FileSharingClient.

    """
    if not args.file:
        print("Please provide a file to upload")
        return
    file_sharing_client.upload_file(args.file)


def handle_download(args, file_sharing_client: FileSharingClient):
    """
    Handle download command.

    Parameters
    ----------
    args : argparse.Namespace
        The parsed command-line arguments.
    file_sharing_client : FileSharingClient
        An instance of the FileSharingClient.

    """
    if not args.file:
        print("Please provide a file to download")
        return

    file_to_download = args.file

    folder = Path(args.output) if args.output else Path("fileshared")
    folder.mkdir(exist_ok=True)

    if folder.is_dir():
        filename = ""
    elif folder.is_file():
        folder, filename = folder.parent, folder.stem
    else:
        print("Invalid output path")
        return

    file_sharing_client.download_file(file_to_download, folder, save_filename=filename)


def handle_downloadl(args, file_sharing_client: FileSharingClient):
    """
    Handle downloadl command.

    Parameters
    ----------
    args : argparse.Namespace
        The parsed command-line arguments.
    file_sharing_client : FileSharingClient
        An instance of the FileSharingClient.

    """
    if not args.nbfiles:
        print("Please provide the number of files to download")
        return

    nb_files = args.nbfiles

    folder = Path(args.output) if args.output else Path("fileshared")
    folder.mkdir(exist_ok=True)

    if folder.is_dir():
        filename = ""
    elif folder.is_file():
        folder, filename = folder.parent, folder.stem
    else:
        print("Invalid output path")
        return

    file_sharing_client.download_last_n_files(nb_files, folder, filename)


def build_cli_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """
    Build CLI parser.

    Parameters
    ----------
    parser : argparse.ArgumentParser
        The ArgumentParser object.

    Returns
    -------
    argparse.ArgumentParser
        The modified ArgumentParser object.

    """
    parser.add_argument(
        "cli_command",
        choices=["login", "logout", "list", "upload", "download", "downloadl"],
        help="Command to execute",
    )
    parser.add_argument(
        "-H",
        "--host",
        help=f"host server: default={DEFAULT_BASE_URL}",
        default=DEFAULT_BASE_URL,
    )
    parser.add_argument("-u", "--username", help="Username")
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument("-f", "--file", help="File to upload or download")
    parser.add_argument("-o", "--output", help="Directory or file path to save the downloaded file")
    parser.add_argument("-n", "--nbfiles", type=int, help="Number of files to list or download")
    parser.add_argument(
        "-r",
        "--order",
        choices=["asc", "desc"],
        help="Order of files to list or download",
    )
    return parser


def parse_args() -> argparse.Namespace:
    """
    Parse CLI arguments.

    Returns
    -------
    argparse.Namespace
        The parsed command-line arguments.

    """
    parser = argparse.ArgumentParser(description="File sharing CLI")
    parser = build_cli_parser(parser)
    args = parser.parse_args()
    return args


def main(args: argparse.Namespace):
    """
    Main function to execute CLI commands.

    Parameters
    ----------
    args : argparse.Namespace
        The parsed command-line arguments.

    """
    if not (args.username and args.password):
        print("Please provide a username and password")
        return

    with client_session_manager(host=args.host, username=args.username,
                                password=args.password) as file_sharing_client:
        assert isinstance(file_sharing_client, FileSharingClient)
        print("\n>>>proceed...\n")

        command_handlers = {
            "login": handle_login,
            "logout": handle_logout,
            "list": handle_list,
            "upload": handle_upload,
            "download": handle_download,
            "downloadl": handle_downloadl,
        }

        handler = command_handlers.get(args.cli_command)

        if not handler:
            raise ValueError(f"Invalid command {args.cli_command}")

        handler(args, file_sharing_client)


if __name__ == "__main__":
    parsed_args = parse_args()
    main(args=parsed_args)
