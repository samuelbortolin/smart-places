from __future__ import absolute_import, annotations

from flask import Flask
from flask_restful import Api

from smartplaces.daos.collector import DaoCollector
from smartplaces.ws.resources import ResourcesBuilder


class WebService:
    """
    The class for configuring and running the web service
    """

    def __init__(self, host: str, port: int, dao_collector: DaoCollector) -> None:
        """
        :param host: the host of the web service
        :param port: the port of the web service
        :param dao_collector: the collector of daos for the management of data
        """

        self._host = host
        self._port = port
        self._dao_collector = dao_collector

        self._app = Flask("smart-places-ws")
        self._api = Api(app=self._app)

        for resource, path, args in ResourcesBuilder.routes(self._dao_collector):
            self._api.add_resource(resource, path, resource_class_args=args)

    def run(self):
        self._app.run(host=self._host, port=self._port)

    def get_application(self):
        return self._app
