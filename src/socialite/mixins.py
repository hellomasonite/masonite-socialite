from importlib import import_module

OAUTH1_PROVIDERS = ['twitter', ]
OAUTH2_PROVIDERS = ['google', 'facebook']


class SocialiteMixin(object):
    __socialite_provider__ = None

    @property
    def socialite_provider(self):
        if self.__socialite_provider__:
            return self.__socialite_provider__

        self.__socialite_provider__ = self.provider

        if '-' in self.provider:
            provider = self.proivder.splite('-')[0]
            self.__socialite_provider__ = provider

        return self.__socialite_provider__

    @property
    def api(self):
        try:
            provider_oauth = import_module(f'socialite.oauth.{self.socialite_provider}')
            provider_class = getattr(provider_oauth, f'{self.socialite_provider.capitalize()}API')
        except ImportError as e:
            raise e

        if self.socialite_provider in OAUTH1_PROVIDERS:
            pass
        elif self.socialite_provider in OAUTH2_PROVIDERS:
            return provider_class.build({"access_token": self.access_token, "token_type": "bearer"})
        else:
            raise NotImplementedError
