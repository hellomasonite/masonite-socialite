"""Web Routes."""

from masonite.routes import Get, Post
from config.socialite import SOCIAL_AUTH_NAMESPACE

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),
    Get(f'/{SOCIAL_AUTH_NAMESPACE}/@backend/login', 'WelcomeController@auth').name('nice'),
    Get(f'/{SOCIAL_AUTH_NAMESPACE}/@backend/callback', 'WelcomeController@callback').name('welcome'),
]
