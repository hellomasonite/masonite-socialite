from socialite.helpers import get_config
from .base import BaseOAuth2


class FacebookAPI(object):

    def __init__(self, token):
        client_id = get_config('socialite.SOCIAL_AUTH_FACEBOOK_KEY')
        self.oauth_session = BaseOAuth2(client_id, token=token)
        self.oauth_session.BASE_URL = 'https://graph.facebook.com'
