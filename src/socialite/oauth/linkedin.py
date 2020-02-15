from masonite.helpers import config

from socialite.oauth.base import BaseOAuth2


class LinkedinAPI(object):
    VERSION = "v2"

    def __init__(self, token, **kwargs):
        client_id = config('socialite', 'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
        self.token = token
        self.oauth_session = BaseOAuth2(client_id, token=token)
        self.oauth_session.BASE_URL = f'https://api.linkedin.com/{self.VERSION}'

    @classmethod
    def build(cls, token):
        return cls(token).oauth_session
