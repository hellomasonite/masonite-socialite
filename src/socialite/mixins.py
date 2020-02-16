import json
from importlib import import_module

OAUTH1_PROVIDERS = ['twitter', ]
OAUTH2_PROVIDERS = ['google', 'facebook', 'linkedin', 'github']


class SocialiteMixin(object):
    __socialite_provider__ = None
    __socialite_api__ = None

    @property
    def socialite_provider(self):
        if self.__socialite_provider__:
            return self.__socialite_provider__

        if not self.provider:
            return None

        self.__socialite_provider__ = self.provider

        if '-' in self.provider:
            provider = self.proivder.splite('-')[0]
            self.__socialite_provider__ = provider

        return self.__socialite_provider__

    @property
    def provider_api(self):
        if self.__socialite_api__:
            return self.__socialite_api__

        try:
            provider_oauth = import_module(f'socialite.oauth.{self.socialite_provider}')
            provider_class = getattr(provider_oauth, f'{self.socialite_provider.capitalize()}API')
        except ImportError as e:
            raise e

        access_token = self.access_token

        if self.socialite_provider in OAUTH1_PROVIDERS:
            if isinstance(access_token, str):
                access_token = json.loads(access_token)

            token = self.__socialite_token_formatter(access_token, oauth_type=1)
            self.__socialite_api__ = provider_class.build(**token)

        elif self.socialite_provider in OAUTH2_PROVIDERS:
            self.__socialite_api__ = provider_class.build(self.__socialite_token_formatter(access_token))
        else:
            raise NotImplementedError

        return self.__socialite_api__

    def __socialite_token_formatter(self, access_token, oauth_type=2):
        if oauth_type == 1:
            return {
                'resource_owner_key': access_token.get('oauth_token'),
                'resource_owner_secret': access_token.get('oauth_token_secret')
            }
        return {
            'access_token': access_token,
            'token_type': 'bearer'
        }
