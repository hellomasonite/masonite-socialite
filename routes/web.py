"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/home', 'WelcomeController@show').name('welcome'),
    Get('/social/@backend/login', 'WelcomeController@auth').name('nice'),
    Get('/social/@backend/callback', 'WelcomeController@callback').name('welcome'),
]
