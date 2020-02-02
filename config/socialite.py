SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
)

SOCIAL_AUTH_FACEBOOK_KEY = ""
SOCIAL_AUTH_FACEBOOK_SECRET = ""

SOCIAL_AUTH_GOOGLE_KEY = ""
SOCIAL_AUTH_GOOGLE_SECRET = ""

# SOCIAL_AUTH_STRATEGY = "socialite.strategy.MasoniteStrategy"

SOCIAL_AUTH_NAMESPACE = "social"

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'email',
}
