# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from crm.models.user import User  # noqa: E501
from crm.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_user_get(self):
        """Test case for user_get

        사용자 조회
        """
        response = self.client.open(
            '/v2/user',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
