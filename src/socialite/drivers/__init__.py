from masonite.request import Request

from .SocialiteBaseDriver import SocialiteBaseDriver


class SocialiteFacebookDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'facebook'
        super().__init__(request)


class SocialiteTwitterDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'twitter'
        super().__init__(request)


class SocialiteGoogleDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'google-oauth2'
        super().__init__(request)


class SocialiteLinkedinDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'linkedin-oauth2'
        super().__init__(request)


class SocialiteGithubDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'github'
        super().__init__(request)
