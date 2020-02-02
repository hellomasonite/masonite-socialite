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
if you want to add more scope, you can use 

```python
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_likes']
```

For more information, please check [here](https://python-social-auth-docs.readthedocs.io/en/latest/backends/index.html)

Add this code to your controller

```python
from masonite.controllers import Controller
from masonite.request import Request

from socialite import Socialite
from socialite.helpers import social_auth


class SocialiteController(Controller):
    """Controller For Social Authentication."""

    @social_auth()
    def login(self, request: Request, socialite: Socialite):
        return socialite.driver('auth').redirect()

    @social_auth()
    def callback(self, request: Request, socialite: Socialite):
        user = socialite.driver('auth').user()
        print(user)
        return request.redirect('/home')
```

* ## user()
The user function, return an user instance that is namedtuple class.
By default, this object has these fields:

```
uid # the user id provides by the provider
fullname  # The full name of user
first_name 
last_name
username
email # if you request for it
raw_data # the default data retrieves from the provider
```

You can now access on by using:
```python
print(user.username)
print(user.first_name)
```

## Helpers
1. **social_auth**

This helper is a decorator that implement the logic of how the backends are 
identified and loaded.


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

The uri routes need to be started by **SOCIAL_AUTH_NAMESPACE**
Without that your callback can be wrong.

```python
SOCIAL_AUTH_NAMESPACE = "social"
```

Visit, [http://localhost:8000/social/facebook/login/](http://localhost:8000/social/facebook/login/)
