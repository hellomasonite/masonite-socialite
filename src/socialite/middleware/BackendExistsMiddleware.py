from masonite.helpers import config
from masonite.request import Request
from social_core.exceptions import MissingBackend

from socialite.helpers import load_strategy, load_backend


class BackendExistsMiddleware:
    def __init__(self, request: Request):
        self.request = request

    def after(self):
        pass

    def before(self):
        backend = self.request.param('backend')
        if hasattr(config('socialite'), 'SOCIAL_AUTH_PREFIX'):
            uri = f"{getattr(config('socialite'), 'SOCIAL_AUTH_PREFIX')}/{backend}"
        else:
            uri = f'{backend}'
        uri = f"{uri}/callback"
        self.request.social_strategy = load_strategy(self.request)
        if not hasattr(self.request, 'strategy'):
            self.request.strategy = self.request.social_strategy

        try:
            self.request.backend = load_backend(self.request.social_strategy, backend, uri)
        except MissingBackend as e:
            return self.request.status(404)
