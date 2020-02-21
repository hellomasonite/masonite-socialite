from socialite.oauth.factory import ProviderFactory


class ProviderAPI:
    def __new__(
            cls,
            name,
            access_token=None,
            resource_owner_key=None,
            resource_owner_secret=None,
            token_type='bearer'
    ):
        return ProviderFactory().make(
            name,
            access_token,
            resource_owner_key,
            resource_owner_secret,
            token_type).oauth_session
