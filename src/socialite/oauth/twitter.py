from socialite.helpers import get_config
from .base import BaseOAuth1


class TwitterAPI(object):
    def __init__(self, resource_owner_key, resource_owner_secret, **kwargs):
        client_id = get_config('socialite.SOCIAL_AUTH_TWITTER_KEY')
        client_secret = get_config('socialite.SOCIAL_AUTH_TWITTER_SECRET')
        self.oauth_session = BaseOAuth1(client_id, client_secret=client_secret, resource_owner_key=resource_owner_key,
                                        resource_owner_secret=resource_owner_secret)
        self.oauth_session.BASE_URL = 'https://api.twitter.com'
