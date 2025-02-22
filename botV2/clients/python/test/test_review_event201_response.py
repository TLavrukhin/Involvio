# coding: utf-8

"""
    api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from random_coffe_client.models.review_event201_response import ReviewEvent201Response

class TestReviewEvent201Response(unittest.TestCase):
    """ReviewEvent201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReviewEvent201Response:
        """Test ReviewEvent201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReviewEvent201Response`
        """
        model = ReviewEvent201Response()
        if include_optional:
            return ReviewEvent201Response(
                event_id = 56,
                grade = 56,
                id = 56,
                who_id = 56,
                whom_id = 56
            )
        else:
            return ReviewEvent201Response(
                event_id = 56,
                grade = 56,
                id = 56,
                who_id = 56,
                whom_id = 56,
        )
        """

    def testReviewEvent201Response(self):
        """Test ReviewEvent201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
