from __future__ import absolute_import, annotations

from unittest import TestCase

from smartplaces.ws.ws import WebService
from tests.unit.smartplaces_tests.ws.common.mocks.daos import MockDaoCollectorBuilder


class CommonWsTestCase(TestCase):
    """
    A common test case for the smart-places web service resources
    """

    def setUp(self) -> None:
        super().setUp()
        self.dao_collector = MockDaoCollectorBuilder.build_mock_daos()
        api = WebService("0.0.0.0", 12345, self.dao_collector)
        api.get_application().testing = True
        self.client = api.get_application().test_client()
