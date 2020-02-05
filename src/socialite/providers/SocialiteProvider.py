"""A SocialiteProvider Service Provider."""

from masonite.provider import ServiceProvider

from socialite import Socialite
from socialite.commands import InstallCommand
from socialite.drivers import *
from socialite.managers import SocialiteManager


class SocialiteProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        self.app.bind('SocialiteGoogleDriver', SocialiteGoogleDriver)
        self.app.bind('SocialiteFacebookDriver', SocialiteFacebookDriver)
        self.app.bind('SocialiteTwitterDriver', SocialiteTwitterDriver)
        self.app.bind('SocialiteGithubDriver', SocialiteGithubDriver)
        self.app.bind('SocialiteLinkedinDriver', SocialiteLinkedinDriver)
        self.app.bind('SocialiteManager', SocialiteManager(self.app))
        self.app.bind('InstallCommand', InstallCommand())

    def boot(self, manager: SocialiteManager):
        """Boots services required by the container."""
        self.app.bind('Socialite', manager)
        self.app.swap(Socialite, manager)
