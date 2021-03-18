from socialite.helpers import get_config
from .base import BaseOAuth2


class AmazonAPI(object):
    def __init__(self, token, **kwargs):
        client_id = get_config("socialite.SOCIAL_AUTH_Amazon_KEY")
        self.oauth_session = BaseOAuth2(client_id, token=token)
        self.oauth_session.BASE_URL = "https://api.amazon.com"