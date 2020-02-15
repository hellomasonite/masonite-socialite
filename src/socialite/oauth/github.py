from masonite.helpers import config

from .base import BaseOAuth2


class GithubAPI(object):

    def __init__(self, token, **kwargs):
        client_id = config('socialite', 'SOCIAL_AUTH_GITHUB_KEY')
        self.token = token
        self.oauth_session = BaseOAuth2(client_id, token=token)
        self.oauth_session.BASE_URL = f'https://api.github.com/'

    @classmethod
    def build(cls, token):
        return cls(token).oauth_session
