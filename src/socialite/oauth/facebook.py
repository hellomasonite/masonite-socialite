from masonite.helpers import config

from .base import BaseOAuth2


class FacebookAPI(object):
    VERSION = "4.0"

    def __init__(self, token):
        client_id = config('socialite.SOCIAL_AUTH_FACEBOOK_KEY')
        client_secret = config('socialite.SOCIAL_AUTH_FACEBOOK_SECRET')
        self.oauth_session = BaseOAuth2(client_id, token=token, client_secret=client_secret)
        self.oauth_session.BASE_URL = f'https://graph.facebook.com/v{self.VERSION}'

    @classmethod
    def build(cls, token):
        return cls(token).oauth_session
