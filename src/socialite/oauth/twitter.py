from masonite.helpers import config

from .base import BaseOAuth1


class TwitterAPI(object):
    def __init__(self, resource_owner_key, resource_owner_secret, **kwargs):
        client_id = config('socialite.SOCIAL_AUTH_TWITTER_KEY')
        client_secret = config('socialite.SOCIAL_AUTH_TWITTER_SECRET')
        self.oauth_session = BaseOAuth1(client_id, client_secret=client_secret, resource_owner_key=resource_owner_key,
                                        resource_owner_secret=resource_owner_secret)
        self.oauth_session.BASE_URL = f'https://api.twitter.com/'

    @classmethod
    def build(cls, resource_owner_key, resource_owner_secret, **kwargs):
        return cls(resource_owner_key, resource_owner_secret).oauth_session
