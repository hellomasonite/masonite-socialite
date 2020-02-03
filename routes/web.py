"""Web Routes."""

from masonite.routes import Get, RouteGroup, Post

from config.socialite import SOCIAL_AUTH_PREFIX

ROUTES = [
    RouteGroup([
        Get(f'/{SOCIAL_AUTH_PREFIX}/@backend/login', 'WelcomeController@auth'),
        Get(f'/{SOCIAL_AUTH_PREFIX}/@backend/callback', 'WelcomeController@callback'),
    ], middleware=('socialite.backend', )),

    Get('/', 'WelcomeController@show').name('welcome'),
]
