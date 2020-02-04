from masonite.helpers import config
from social_core.backends.utils import get_backend
from social_core.utils import setting_name, module_member


BACKENDS = getattr(config('socialite'), 'SOCIAL_AUTH_AUTHENTICATION_BACKENDS', [])
STRATEGY = getattr(config('socialite'), setting_name('STRATEGY'),
                   'socialite.strategy.MasoniteStrategy')


def get_strategy(strategy, storage, *args, **kwargs):
    strategy = module_member(strategy)
    return strategy(request=args[0], *args, **kwargs)


def load_strategy(request=None):
    return get_strategy(STRATEGY, None, request)


def load_backend(strategy, name, redirect_uri):
    backend = get_backend(BACKENDS, name)
    return backend(strategy, redirect_uri)
