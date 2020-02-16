from masonite.request import Request

from .SocialiteBaseDriver import SocialiteBaseDriver

AVAILABLE_PROVIDERS = [
    'github', 'facebook',
    'twitter', 'google',
    'linkedin', 'gitlab',
    'bitbucket', 'trello',
    'slack', 'instagram',
    'dropbox', 'pinterest'
]


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


class SocialiteGitlabDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'gitlab'
        super().__init__(request)


class SocialiteBitbucketDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'bitbucket-oauth2'
        super().__init__(request)


class SocialiteSlackDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'slack'
        super().__init__(request)


class SocialiteInstagramDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'instagram'
        super().__init__(request)


class SocialiteDropboxDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'dropbox-oauth2'
        super().__init__(request)


class SocialiteTrelloDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'trello'
        super().__init__(request)


class SocialitePinterestDriver(SocialiteBaseDriver):
    def __init__(self, request: Request):
        self.name = 'pinterest'
        super().__init__(request)
