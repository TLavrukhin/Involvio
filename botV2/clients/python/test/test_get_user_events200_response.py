# coding: utf-8

"""
    api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from random_coffe_client.models.get_user_events200_response import GetUserEvents200Response

class TestGetUserEvents200Response(unittest.TestCase):
    """GetUserEvents200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUserEvents200Response:
        """Test GetUserEvents200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUserEvents200Response`
        """
        model = GetUserEvents200Response()
        if include_optional:
            return GetUserEvents200Response(
                body = random_coffe_client.models.user_events_response_body.UserEventsResponseBody(
                    events = [
                        random_coffe_client.models.event.Event(
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            id = 56, 
                            name = '', 
                            users = [
                                random_coffe_client.models.user.User(
                                    birthday = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    city = '', 
                                    full_name = '', 
                                    gender = '', 
                                    goal = '', 
                                    groups = [
                                        random_coffe_client.models.group.Group(
                                            id = 56, 
                                            name = '', )
                                        ], 
                                    id = 56, 
                                    interests = '', 
                                    photo_url = '', 
                                    position = '', 
                                    socials = '', 
                                    user_name = '', )
                                ], )
                        ], )
            )
        else:
            return GetUserEvents200Response(
                body = random_coffe_client.models.user_events_response_body.UserEventsResponseBody(
                    events = [
                        random_coffe_client.models.event.Event(
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            id = 56, 
                            name = '', 
                            users = [
                                random_coffe_client.models.user.User(
                                    birthday = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    city = '', 
                                    full_name = '', 
                                    gender = '', 
                                    goal = '', 
                                    groups = [
                                        random_coffe_client.models.group.Group(
                                            id = 56, 
                                            name = '', )
                                        ], 
                                    id = 56, 
                                    interests = '', 
                                    photo_url = '', 
                                    position = '', 
                                    socials = '', 
                                    user_name = '', )
                                ], )
                        ], ),
        )
        """

    def testGetUserEvents200Response(self):
        """Test GetUserEvents200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
