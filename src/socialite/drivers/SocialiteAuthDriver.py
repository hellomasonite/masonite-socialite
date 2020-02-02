from collections import namedtuple

from masonite.drivers import BaseDriver
from masonite.request import Request
from social_core.actions import do_auth

from socialite.actions import do_complete


class SocialiteAuthDriver(BaseDriver):
    def __init__(self, request: Request):
        self.request = request
        self.backend = request.backend

    def _auth(self):
        return do_auth(self.backend)

    def _complete(self):
        user_formatted_data, response = do_complete(self.backend)
        user_formatted_data["access_token"] = response.get("access_token", "")
        user_formatted_data['uid'] = response.get("id", "")
        user_formatted_data["raw_data"] = response
        user_formatted_data['provider'] = self.backend.name
        user = namedtuple("User", user_formatted_data.keys())(*user_formatted_data.values())
        return user

    def redirect(self):
        return self._auth()

    def user(self):
        user = self._complete()
        return user
