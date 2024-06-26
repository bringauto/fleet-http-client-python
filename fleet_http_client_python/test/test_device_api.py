# coding: utf-8

"""
    Fleet v2 HTTP API

    HTTP-based API for Fleet Protocol v2 serving for communication between the External Server and the end users.

    The version of the OpenAPI document: 2.2.0
    Contact: jiri.strouhal@bringauto.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fleet_http_client_python.api.device_api import DeviceApi


class TestDeviceApi(unittest.TestCase):
    """DeviceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DeviceApi()

    def tearDown(self) -> None:
        pass

    def test_list_commands(self) -> None:
        """Test case for list_commands

        """
        pass

    def test_list_statuses(self) -> None:
        """Test case for list_statuses

        """
        pass

    def test_send_commands(self) -> None:
        """Test case for send_commands

        """
        pass

    def test_send_statuses(self) -> None:
        """Test case for send_statuses

        """
        pass


if __name__ == '__main__':
    unittest.main()
