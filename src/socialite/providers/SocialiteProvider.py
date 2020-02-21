"""A SocialiteProvider Service Provider."""
from importlib import import_module

from masonite.provider import ServiceProvider

from socialite import Socialite
from socialite.commands import InstallCommand
from socialite.drivers import AVAILABLE_PROVIDERS
from socialite.managers import SocialiteManager


class SocialiteProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        drivers = import_module('socialite.drivers')
        for provider in AVAILABLE_PROVIDERS:
            driver_name = 'Socialite{provider}Driver'.format(provider=provider.capitalize())
            self.app.bind(driver_name, getattr(drivers, driver_name))
        self.app.bind('SocialiteManager', SocialiteManager(self.app))
        self.app.bind('InstallCommand', InstallCommand())

    def boot(self, manager: SocialiteManager):
        """Boots services required by the container."""
        self.app.bind('Socialite', manager)
        self.app.swap(Socialite, manager)
