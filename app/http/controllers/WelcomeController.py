"""Welcome The User To Masonite."""
import json

from masonite.auth import Auth
from masonite.controllers import Controller
from masonite.request import Request
from masonite.view import View

from app.User import User
from socialite import Socialite


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

    def auth(self, request: Request, socialite: Socialite):
        return socialite.driver(request.param('provider')).redirect()

    def callback(self, request: Request, socialite: Socialite, auth: Auth):
        user_info = socialite.driver(request.param('provider')).user()

        user = User.first_or_create(
            email=user_info.email,
            name=user_info.username,
            access_token=json.dumps(user_info.access_token) if isinstance(user_info.access_token,
                                                                          dict) else user_info.access_token,
            provider=user_info.provider)
        auth.once().login_by_id(user.id)
        return request.redirect('/')
