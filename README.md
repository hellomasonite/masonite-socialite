# Masonite Socialite
Make social authentication with all providers supported by 
[social-auth-core](https://github.com/python-social-auth/social-core) package.

## Installation

```bash
pip install -e .
```

## Configuration
Import the **SocialiteProvider** to your application in *config.providers*

```python
from socialite.providers import SocialiteProvider

PROVIDERS = [
    ...
    SocialiteProvider
    ...
]
```

After that craft the socialite config by running:
```bash
craft socialite:install
```

## Usage
Configure your credentials for the provider you want to use.

```python
SOCIAL_AUTH_FACEBOOK_KEY = "YOUR_FACEBOOK_APP_ID"
SOCIAL_AUTH_FACEBOOK_SECRET = "YOUR_FACEBOOK_APP_SECRET"
```

Create a new controller by running:

```bash
craft controller SocialiteController
```

Add this code to your controller

```python
from masonite.controllers import Controller
from masonite.request import Request

from socialite import Socialite
from socialite.helpers import social_auth


class SocialiteController(Controller):
    """Controller For Welcoming The User."""

    @social_auth()
    def login(self, request: Request, socialite: Socialite):
        return socialite.driver('auth').redirect()

    @social_auth()
    def callback(self, request: Request, socialite: Socialite):
        user = socialite.driver('auth').user()
        print(user)
        return request.redirect('/home')
```

Now you need to define the routes in the **routes/web.py**:

```python
from config.socialite import SOCIAL_AUTH_NAMESPACE

ROUTES = [
    ...
    Get(f'/{SOCIAL_AUTH_NAMESPACE}/@backend/login', 'SocialiteController@login').name('social.login'),
    Get(f'/{SOCIAL_AUTH_NAMESPACE}/@backend/callback', 'SocialiteController@callback').name('social.callback'),
    ...
]
```

Visit, [http://localhost:8000/social/facebook/login/](http://localhost:8000/social/facebook/login/)
