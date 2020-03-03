from socialite.exceptions import ProviderAPIDoesNotExistsError
from socialite.oauth.facebook import FacebookAPI
from socialite.oauth.github import GithubAPI
from socialite.oauth.google import GoogleAPI
from socialite.oauth.linkedin import LinkedinAPI
from socialite.oauth.twitter import TwitterAPI


class ProviderFactory:
    providers = {
        'github': GithubAPI,
        'facebook': FacebookAPI,
        'twitter': TwitterAPI,
        'linkedin': LinkedinAPI,
        'google': GoogleAPI,
    }

    __socialite_api__ = None

    _oauth1_providers = ['twitter', ]
    _oauth2_providers = ['google', 'facebook', 'linkedin', 'github']

    _provider_type = None

    @classmethod
    def make(cls, name, access_token=None, resource_owner_key=None, resource_owner_secret=None, token_type='bearer'):
        cls.name = name.split("-")[0]

        if cls.name in cls._oauth1_providers:
            assert resource_owner_secret, "Missing required 'resource_owner_secret' parameter"
            assert resource_owner_key, "Missing required 'resource_owner_key' parameter"
            cls._provider_type = 'oauth1'
        elif cls.name in cls._oauth2_providers:
            assert access_token, "Missing required 'access_token' parameter"
            cls._provider_type = 'oauth2'
        else:
            raise ProviderAPIDoesNotExistsError("The provider '{name}' doesn't supported".format(name=name))

        cls.access_token = access_token
        cls.resource_owner_key = resource_owner_key
        cls.resource_owner_secret = resource_owner_secret

        if cls._provider_type == 'oauth1':
            cls.__socialite_api__ = cls.providers.get(cls.name)(cls.resource_owner_key, cls.resource_owner_secret)
        elif cls._provider_type == 'oauth2':
            cls.__socialite_api__ = cls.providers.get(cls.name)({
                'token_type': token_type,
                'access_token': cls.access_token
            })
        return cls.__socialite_api__
