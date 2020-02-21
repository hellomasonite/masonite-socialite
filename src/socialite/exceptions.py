class InvalidRedirectUriError(Exception):
    """If the redirect uri is not set for the provider"""


class ProviderAPIDoesNotExistsError(Exception):
    """ if the provider is not supported """
