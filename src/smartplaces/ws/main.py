from __future__ import absolute_import, annotations

import argparse
import os

from smartplaces.daos.collector import DaoCollector
from smartplaces.ws.ws import WebService


if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser(description="Smart-Places web service")
    arg_parser.add_argument("-wh", "--host", default=os.getenv("WS_HOST", "0.0.0.0"), type=str, help="The web service host")
    arg_parser.add_argument("-wp", "--port", default=int(os.getenv("WS_PORT", 12345)), type=int, help="The web service port")
    args = arg_parser.parse_args()

    dao_collector = DaoCollector.build_memory_daos()
    ws = WebService(args.host, args.port, dao_collector)

    try:
        ws.run()
    except KeyboardInterrupt:
        exit()
