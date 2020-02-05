"""Web Routes."""

from masonite.routes import Get, RouteGroup

ROUTES = [
    RouteGroup([
        Get('/social/@backend/login', 'WelcomeController@auth'),
        Get('/social/@backend/callback', 'WelcomeController@callback'),
    ]),

    Get('/', 'WelcomeController@show').name('welcome'),
]
