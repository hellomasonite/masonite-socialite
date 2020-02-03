"""A InstallCommand Command for Masonite Socialite."""
import os

from cleo import Command
from masonite.packages import create_or_append_config

package_directory = os.path.dirname(os.path.realpath(__file__))


class InstallCommand(Command):
    """
    Craft the socialite config file

    socialite:install
    """

    def handle(self):
        create_or_append_config(
            os.path.join(
                package_directory,
                '../config/socialite.py'
            )
        )
