from __future__ import absolute_import, annotations

from flask import Flask
from flask_restful import Api

from smartplaces.ws.resources import ResourcesBuilder


class WebService:

    def __init__(self, host: str = "0.0.0.0", port: int = 12345) -> None:
        self._host = host
        self._port = port

        self._app = Flask("smart-places-ws")
        self._api = Api(app=self._app)

        for resource, path, args in ResourcesBuilder.routes():
            self._api.add_resource(resource, path, resource_class_args=args)

    def run(self):
        self._app.run(host=self._host, port=self._port)
