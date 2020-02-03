# Masonite Socialite
🤖 Flexible Social Authentication for Masonite Framework.

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


class SocialiteController(Controller):
    """Controller For Social Authentication."""

    def login(self, request: Request, socialite: Socialite):
        return socialite.driver('auth').redirect()

    def callback(self, request: Request, socialite: Socialite):
        user = socialite.driver('auth').user()
        print(user)
        return request.redirect('/home')
```

The user function, return an user instance that is namedtuple class. 
For example, for a github authentication, we have:

```python
User(
  username='corentinalcoy', 
  email='example@example.com', 
  fullname='', 
  first_name='', 
  last_name='', 
  access_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  uid=51742802, 
  raw_data={
    'access_token': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
    'token_type': 'bearer', 
    'scope': 'user:email', 
    'login': 'corentinalcoy', 
    'id': 51742802, 
    'node_id': 'MDQ6VXNlcjUxNzQyODAy', 
    'avatar_url': 'https://avatars3.githubusercontent.com/u/51742802?v=4', 
    'gravatar_id': '', 
    'url': 'https://api.github.com/users/corentinalcoy', 
    'html_url': 'https://github.com/corentinalcoy', 
    'followers_url': 'https://api.github.com/users/corentinalcoy/followers', 
    'following_url': 'https://api.github.com/users/corentinalcoy/following{/other_user}', 
    'gists_url': 'https://api.github.com/users/corentinalcoy/gists{/gist_id}', 
    'starred_url': 'https://api.github.com/users/corentinalcoy/starred{/owner}{/repo}', 	
    'subscriptions_url': 'https://api.github.com/users/corentinalcoy/subscriptions', 
    'organizations_url': 'https://api.github.com/users/corentinalcoy/orgs', 
    'repos_url': 'https://api.github.com/users/corentinalcoy/repos', 
    'events_url': 'https://api.github.com/users/corentinalcoy/events{/privacy}', 
    'received_events_url': 'https://api.github.com/users/corentinalcoy/received_events', 
    'type': 'User', 
    'site_admin': False, 'name': None, 
    'company': None, 'blog': '', 'location': None, 
    'email': 'example@example.com', 
    'hireable': None, 'bio': None, 
    'public_repos': 21, 
    'public_gists': 0, 
    'followers': 0, 
    'following': 4, 
    'created_at': '2019-06-12T09:32:06Z', 
    'updated_at': '2020-01-30T17:31:51Z'
  }, 
  provider='github'
)
```

You can now access on by using:
```python
print(user.username)
print(user.first_name)
```

Now you need to define the routes in the **routes/web.py**:

```python
from masonite.routes import Get, RouteGroup, Post

from config.socialite import SOCIAL_AUTH_PREFIX

ROUTES = [
    ....
    RouteGroup([
        Get(f'/{SOCIAL_AUTH_PREFIX}/@backend/login', 'SocialiteController@auth'),
        Get(f'/{SOCIAL_AUTH_PREFIX}/@backend/callback', 'SocialiteController@callback'),
    ], middleware=('socialite.backend', )),
    ....
]

```

The uri routes need to be started by **SOCIAL_AUTH_PREFIX**
Without that your callback may be wrong.

```python
SOCIAL_AUTH_NAMESPACE = "social"
```

Visit, [http://localhost:8000/social/facebook/login/](http://localhost:8000/social/facebook/login/)
