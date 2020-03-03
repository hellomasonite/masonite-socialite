<h1 align="center">Masonite Socialite</h1>

<div align="center">
  <strong>Flexible Social Authentication for Masonite Framework</strong>
</div>

<div align="center">
  <h3>
    <a href="https://www.hellomasonite.com/">
      Read our Blog
    </a>
    <span> | </span>
    <a href="https://twitter.com/HelloMasonite">
      Follow us on Twitter
    </a>
  </h3>
</div>

## Table of Contents
- [Example](#example)
- [Installation](#installation)
- [Configuration](#configuration)
- [Routing](#routing)
- [Controllers](#controllers)
- [Providers](#providers)
- [Support](#support)

## Example
```python
class SocialAuthController(Controller):
    """SocialAuthController Controller Class."""

    def login(self, socialite: Socialite):
        return socialite.driver('github').redirect()

    def callback(self, view: View, request: Request, socialite: Socialite):
        user = socialite.driver('github').user()
        # Your application logic here.
```

## Installation

```sh
# Using pip
$ pip install masonite-socialite

# Using Pipenv
$ pipenv install masonite-socialite

# Using Poetry
$ poetry add masonite-socialite
```

Add `SocialiteProvider` to your provider list in `config/providers.py`:

```python
from socialite.providers import SocialiteProvider

PROVIDERS = [

    # Third Party Providers
    SocialiteProvider,
]
```

This will add a new `socialite:install` command to craft. Then run in your terminal:

```bash
craft socialite:install
```

## Configuration

Before using Socialite, you need to get credentials from the provider(s) you want to use. Depending on the providers your application requires, you'll put the right credentials in the `.env` file:

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

If you don't know how to get those values, you can find a detailed guide [here](GUIDE.md).

## Routing

You need two routes: one for redirecting the user to the appropriate OAuth provider, and another for receiving the callback from the provider after authentication.

```python
"""Web Routes."""

from masonite.routes import Get, RouteGroup

ROUTES = [
    Get('auth/@provider', 'SocialAuthController@login'),
    Get('auth/@provider/callback', 'SocialAuthController@callback'),
]
```

## Controllers

You can access `Socialite` using the Socialite helper:

```python
from masonite.auth import Auth
from masonite.controllers import Controller
from masonite.request import Request

from app.User import User
from socialite import Socialite



class SocialAuthController(Controller):
    """Controller For Social Authentication."""

    def redirect_to_provider(self, request: Request, socialite: Socialite):
        """Redirect the user to the authentication page"""
        return socialite.driver(request.provider).redirect()

    def handle_provider_callback(self, request: Request, socialite: Socialite, auth: Auth):
        """Obtain the user information"""
        user = socialite.driver(request.provider).user()
        # => print(user)
        return request.redirect('/home')

```

## Providers

- [x] Github
- [x] Facebook
- [x] Twitter
- [x] Google
- [x] Linkedin
- [ ] Gitlab

We are accepting new providers. Send new provider pull requests. You can follow this tutorial to add a new provider.

## Support
Creating a quality framework takes a lot of time. Unlike others frameworks,
Masonite Socialite is completely independently funded. We fight for our users. This does mean
however that we also have to spend time working contracts to pay the bills.
This is where you can help: by chipping in you can ensure more time is spent
improving Masonite Socialite rather than dealing with distractions.
