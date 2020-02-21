from socialite.helpers import get_config
from .base import BaseOAuth2


class GithubAPI(object):

    def __init__(self, token, **kwargs):
        client_id = get_config('socialite.SOCIAL_AUTH_GITHUB_KEY')
        self.oauth_session = BaseOAuth2(client_id, token=token)
        self.oauth_session.BASE_URL = 'https://api.github.com'
