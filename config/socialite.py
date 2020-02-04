"""Masonite Socialite Config file"""

from masonite import env

""" The default strategy you need to use. You can write your own strategy """

# SOCIAL_AUTH_STRATEGY = "socialite.strategy.MasoniteStrategy"

"""
 The default namespace. Your routes for the social login should start by this namepsace, 
 otherwise your callback may be wrong.
"""

SOCIAL_AUTH_PREFIX = "social"

"""
 The list of the providers you need to support in your project. 
 More information about the available backends at https://python-social-auth.readthedocs.io/en/latest/backends/index.html
"""

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
)

"""
 FACEBOOK Configurations
"""

SOCIAL_AUTH_FACEBOOK_KEY = env("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = env("SOCIAL_AUTH_FACEBOOK_SECRET")
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email',
}


"""
 Google Configurations
"""

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
