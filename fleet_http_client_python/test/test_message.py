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

from fleet_http_client_python.models.message import Message

class TestMessage(unittest.TestCase):
    """Message unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Message:
        """Test Message
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Message`
        """
        model = Message()
        if include_optional:
            return Message(
                timestamp = 1699262836,
                device_id = {"module_id":47,"type":2,"role":"test_device","name":"Test Device"},
                payload = {"message_type":"STATUS","encoding":"BASE64","data":"QnJpbmdBdXRv"}
            )
        else:
            return Message(
                device_id = {"module_id":47,"type":2,"role":"test_device","name":"Test Device"},
                payload = {"message_type":"STATUS","encoding":"BASE64","data":"QnJpbmdBdXRv"},
        )
        """

    def testMessage(self):
        """Test Message"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()