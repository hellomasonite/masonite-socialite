from functools import wraps

from social_core.backends.utils import get_backend
from social_core.exceptions import MissingBackend
from social_core.utils import setting_name, module_member

from config import socialite

BACKENDS = getattr(socialite, 'SOCIAL_AUTH_AUTHENTICATION_BACKENDS')
STRATEGY = getattr(socialite, setting_name('STRATEGY'),
                   'socialite.strategy.MasoniteStrategy')


def get_strategy(strategy, storage, *args, **kwargs):
    strategy = module_member(strategy)
    return strategy(request=args[0], *args, **kwargs)


def load_strategy(request=None):
    return get_strategy(STRATEGY, None, request)


def load_backend(strategy, name, redirect_uri):
    backend = get_backend(BACKENDS, name)
    return backend(strategy, redirect_uri)


def social_auth(load_strategy=load_strategy):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            view = args[0]
            request = args[1]
            manager = args[2]
            backend = request.param('backend')
            if hasattr(socialite, 'SOCIAL_AUTH_NAMESPACE'):
                uri = f"{getattr(socialite, 'SOCIAL_AUTH_NAMESPACE')}/{backend}"
            else:
                uri = f'{backend}'
            uri = f"{uri}/callback"
            request.social_strategy = load_strategy(request)
            if not hasattr(request, 'strategy'):
                request.strategy = request.social_strategy

            try:
                request.backend = load_backend(request.social_strategy,
                                               backend, uri)
            except MissingBackend as e:
                raise e
            return func(self=view, request=request, socialite=manager)

        return wrapper

    return decorator
