from socialite.helpers import get_config
from socialite.oauth.base import BaseOAuth2


class LinkedinAPI(object):

    def __init__(self, token, **kwargs):
        client_id = get_config('socialite.SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY')
        self.oauth_session = BaseOAuth2(client_id, token=token)
        self.oauth_session.BASE_URL = 'https://api.linkedin.com'
