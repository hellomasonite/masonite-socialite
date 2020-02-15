"""User Model."""

from config.database import Model
from socialite.mixins import SocialiteMixin


class User(Model, SocialiteMixin):
    """User Model."""

    __fillable__ = ['name', 'email', 'password', 'provider', 'access_token']

    __auth__ = 'email'
