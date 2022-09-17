import sys
import time

from . import cli

# Currently this is what triggers all the argparse construction, so its slow:
start = time.time()
from . import client

end = time.time()
cli.debug(f"DEBUG: {int(1000*(end-start))}ms | from . import client")


def main():

    start = time.time()
    cli.run(sys.argv[1:])
    end = time.time()
    cli.debug(f"DEBUG: {int(1000*(end-start))}ms | main()")
