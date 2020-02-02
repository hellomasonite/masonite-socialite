"""A SocialiteProvider Service Provider."""

from masonite.provider import ServiceProvider

from socialite import Socialite
from socialite.SocialiteManager import SocialiteManager
from socialite.drivers import SocialiteAuthDriver
from socialite.commands import InstallCommand


class SocialiteProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        self.app.bind('SocialiteConfig', {})
        self.app.bind('SocialiteAuthDriver', SocialiteAuthDriver)
        self.app.bind('SocialiteManager', SocialiteManager(self.app))
        self.app.bind('InstallCommand', InstallCommand())

    def boot(self, manager: SocialiteManager):
        """Boots services required by the container."""
        self.app.bind('Socialite', manager)
        self.app.swap(Socialite, manager)
