from collections import namedtuple

from masonite.drivers import BaseDriver
from masonite.helpers import config
from masonite.request import Request
from social_core.actions import do_auth
from social_core.exceptions import MissingBackend

from socialite.actions import do_complete
from socialite.exceptions import InvalidRedirectUriError
from socialite.helpers import load_strategy, load_backend


class SocialiteBaseDriver(BaseDriver):
    def __init__(self, request: Request):
        self.request = request
        self._load_backend_and_strategy()
        self.backend_str = None

    def _auth(self):
        return do_auth(self.request.backend)

    def _complete(self):
        user_formatted_data, response = do_complete(self.request.backend)
        user_formatted_data["access_token"] = response.get("access_token", "")
        user_formatted_data['uid'] = response.get("id", "")
        user_formatted_data["raw_data"] = response
        user_formatted_data['provider'] = self.request.backend.name
        user = namedtuple("User", user_formatted_data.keys())(*user_formatted_data.values())
        return user

    def redirect(self):
        return self._auth()

    def user(self):
        user = self._complete()
        return user

    def _load_backend_and_strategy(self):
        redirect_uri = self._get_redirect_uri()

        self.request.social_strategy = load_strategy(self.request)

        if not hasattr(self.request, 'strategy'):
            self.request.strategy = self.request.social_strategy

        try:
            self.request.backend = load_backend(self.request.social_strategy, self.name, redirect_uri)
        except MissingBackend as e:
            return self.request.status(404)

    def _get_redirect_uri(self):
        self.backend_str = self.name
        if '-' in self.name:
            self.backend_str = "_".join(self.name.split("-"))
        return self.format_redirect(
            getattr(config('socialite'), f'SOCIAL_AUTH_{self.backend_str.upper()}_REDIRECT_URI', None))

    def format_redirect(self, redirect: str):
        if not redirect:
            raise InvalidRedirectUriError(f'SOCIAL_AUTH_{self.backend_str.upper()}_REDIRECT_URI doesn\'t exists')

        if redirect.startswith('/'):
            app_url = config('application.URL')
            redirect = f'{app_url.url}{redirect}' if app_url.endswith('/') else f'{app_url}/{redirect}'
        return redirect
