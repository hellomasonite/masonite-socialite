"""User Model."""

from config.database import Model
from socialite.api import ProviderAPI


class User(Model):
    """User Model."""

    __fillable__ = ['name', 'email', 'password', 'provider', 'access_token']

    __auth__ = 'email'

    @property
    def api(self):
        return ProviderAPI(self.provider, access_token=self.access_token)
