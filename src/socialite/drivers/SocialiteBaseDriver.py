from collections import namedtuple

from masonite.drivers import BaseDriver
from masonite.request import Request
from social_core.actions import do_auth
from social_core.exceptions import MissingBackend

from socialite.actions import do_complete
from socialite.exceptions import InvalidRedirectUriError
from socialite.helpers import load_strategy, load_backend, get_config


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
        user_formatted_data['provider'] = self.request.backend.name.split('-')[0]
        user_info = namedtuple("User", user_formatted_data.keys())(*user_formatted_data.values())
        return user_info

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
        return self._format_redirect(
                get_config('socialite.SOCIAL_AUTH_{provider_name}_REDIRECT_URI'
                           .format(provider_name=self.backend_str.upper())))

    def _format_redirect(self, redirect: str):
        if not redirect:
            raise InvalidRedirectUriError(
                'SOCIAL_AUTH_{provider_name}_REDIRECT_URI '
                'doesn\'t exists'.format(provider_name=self.backend_str.upper())
            )

        if redirect.startswith('/'):
            app_url = get_config('application.URL')
            redirect = '{url}{redirect}'.format(url=app_url, redirect=redirect) if app_url.endswith('/') \
                else '{app_url}/{redirect}'.format(app_url=app_url, redirect=redirect)
        return redirect
