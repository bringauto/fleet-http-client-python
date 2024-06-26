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

from fleet_http_client_python.api.login_api import LoginApi


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LoginApi()

    def tearDown(self) -> None:
        pass

    def test_login(self) -> None:
        """Test case for login

        """
        pass

    def test_token_get(self) -> None:
        """Test case for token_get

        """
        pass

    def test_token_refresh(self) -> None:
        """Test case for token_refresh

        """
        pass


if __name__ == '__main__':
    unittest.main()
