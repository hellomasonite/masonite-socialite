# Masonite Socialite

> Flexible Social Authentication for Masonite Framework

Masonite Socialite is an authentication package for Masonite Framework. Extremely flexible and modular, Masonite Socialite supports authentication with Facebook, Twitter, Github, LinkedIn, Google and more.

Here's a demo of how you can use it:

## Installation

You can install the package via `pip`:

```bash
pip install masonite-socialite
```

## Configuration

Add the Service Provider to your provider list in `config/providers.py`:

```python
from socialite.providers import SocialiteProvider

PROVIDERS = [

    # Third Party Providers
    SocialiteProvider,
]
```

This will add a new socialite:install command to craft. Just run:

```bash
craft socialite:install
```

## Usage

1. Configure your OAuth keys for the provider you want to use in your `.env` file.

```python
# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''
SOCIAL_AUTH_FACEBOOK_REDIRECT_URI = ''

# Twitter
SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''
SOCIAL_AUTH_TWITTER_REDIRECT_URI = ''

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = ''

# Github
SOCIAL_AUTH_GITHUB_KEY = ''
SOCIAL_AUTH_GITHUB_SECRET = ''
SOCIAL_AUTH_GITHUB_REDIRECT_URI = ''

# LinkedIn
SOCIAL_AUTH_LINKEDIN_KEY = ''
SOCIAL_AUTH_LINKEDIN_SECRET = ''
SOCIAL_AUTH_LINKEDIN_OAUTH2_REDIRECT_URI = ''
```

2. In your controller, `SocialAuthController` for example, put the following code:

```python
from masonite.controllers import Controller
from masonite.request import Request

from socialite import Socialite


class SocialAuthController(Controller):
    """Controller For Social Authentication."""

    def redirect_to_provider(self, request: Request, socialite: Socialite):
        """Redirect the user to the authentication page"""
        return socialite.driver(request.param('provider')).redirect()

    def handle_provider_callback(self, request: Request, socialite: Socialite):
        """Obtain the user information"""
        user = socialite.driver(request.param('provider')).user()
        # => print(user)
        return request.redirect('/home')
```

The ```request.param('provider')``` represents the name of the provider.

3. You need to define the routes:

```python
from masonite.routes import Get, RouteGroup


ROUTES = [
    RouteGroup([
        Get(f'/oauth/@provider/login', 'SocialAuthController@redirect_to_provider'),
        Get(f'/oauth/@provider/callback', 'SocialAuthController@handle_provider_callback'),
    ]),
]
```

Visit, [http://localhost:8000/oauth/facebook/login/](http://localhost:8000/social/facebook/login/)
