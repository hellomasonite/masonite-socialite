"""Welcome The User To Masonite."""

from masonite.controllers import Controller
from masonite.request import Request
from masonite.view import View

from socialite import Socialite
from socialite.helpers import social_auth


class WelcomeController(Controller):
    """Controller For Welcoming The User."""

    def show(self, view: View, request: Request):
        """Show the welcome page.

        Arguments:
            view {masonite.view.View} -- The Masonite view class.
            request {masonite.request.Request} -- The Masonite request class.

        Returns:
            masonite.view.View -- The Masonite view class.
        """
        return view.render('welcome')

    @social_auth()
    def auth(self, request: Request, socialite: Socialite):
        return socialite.driver('auth').redirect()

    @social_auth()
    def callback(self, request: Request, socialite: Socialite):
        user = socialite.driver('auth').user()
        return request.redirect('/')
