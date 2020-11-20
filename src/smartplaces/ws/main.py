from __future__ import absolute_import, annotations

import argparse
import os

from smartplaces.ws.ws import WebService


if __name__ == "__main__":

    argParser = argparse.ArgumentParser(description="Smart-Places web service")
    argParser.add_argument("-wh", "--host", default=os.getenv("WS_HOST", "0.0.0.0"), type=str, help="The web service host")
    argParser.add_argument("-wp", "--port", default=int(os.getenv("WS_PORT", 12345)), type=int, help="The web service port")

    args = argParser.parse_args()

    ws = WebService(args.host, args.port)

    try:
        ws.run()
    except KeyboardInterrupt:
        exit()
