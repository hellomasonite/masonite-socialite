from masonite.helpers import config

from .base import BaseOAuth2


class GoogleAPI(object):

    def __init__(self, token, **kwargs):
        client_id = config('socialite.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
        client_secret = config('socialite.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
        self.oauth_session = BaseOAuth2(client_id, client_secret=client_secret, token=token)
        self.oauth_session.BASE_URL = f'https://www.googleapis.com/'

    @classmethod
    def build(cls, token):
        return cls(token).oauth_session
