from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth2Session


class BaseOAuth1(OAuth1Session):
    BASE_URL = None

    def _build_uri(self, uri: str):
        if not uri:
            return None
        elif uri.startswith('https://'):
            return uri
        else:
            if uri.startswith('/'):
                uri = uri[1:]
            return '{BASE_URL}/{uri}'.format(BASE_URL=self.BASE_URL, uri=uri)

    def request(self, method, url, **kwargs):
        url = self._build_uri(url)
        return super(BaseOAuth1, self).request(method=method, url=url, **kwargs)


class BaseOAuth2(OAuth2Session):
    BASE_URL = None

    def _build_uri(self, uri: str):
        if not uri:
            return None
        elif uri.startswith('https://'):
            return uri
        else:
            if uri.startswith('/'):
                uri = uri[1:]
            return '{BASE_URL}/{uri}'.format(BASE_URL=self.BASE_URL, uri=uri)

    def request(
            self,
            method,
            url,
            data=None,
            headers=None,
            withhold_token=False,
            client_id=None,
            client_secret=None,
            **kwargs
    ):
        url = self._build_uri(url)
        return super(BaseOAuth2, self).request(
            method=method,
            url=url,
            data=data,
            headers=headers,
            withhold_token=withhold_token,
            client_id=client_id,
            client_secret=client_secret,
            **kwargs
        )
