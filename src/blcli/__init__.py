import sys

from . import cli, client


def main():
    cli.run(sys.argv[1:])
