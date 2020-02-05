"""Web Routes."""

from masonite.routes import Get, RouteGroup

ROUTES = [
    RouteGroup([
        Get('/social/@provider/login', 'WelcomeController@auth'),
        Get('/social/@provider/callback', 'WelcomeController@callback'),
    ]),

    Get('/', 'WelcomeController@show').name('welcome'),
]
