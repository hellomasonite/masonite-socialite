from masonite.testing import TestCase

from socialite.api import ProviderAPI


class TestProviderAPI(TestCase):
    def test_twitter_provider(self):
        api = ProviderAPI('twitter', resource_owner_key='xxxxxxxxx', resource_owner_secret='vvvvvvvvv')
        self.assertEqual('https://api.twitter.com', api.BASE_URL)

    def test_facebook_provider(self):
        api = ProviderAPI('facebook', access_token='xxxxxxxxx')
        self.assertEqual('https://graph.facebook.com', api.BASE_URL)

    def test_github_provider(self):
        api = ProviderAPI('github', access_token='xxxxxxxxx')
        self.assertEqual('https://api.github.com', api.BASE_URL)

    def test_google_provider(self):
        api = ProviderAPI('google', access_token='xxxxxxxxx')
        self.assertEqual('https://www.googleapis.com', api.BASE_URL)

    def test_linkedin_provider(self):
        api = ProviderAPI('linkedin', access_token='xxxxxxxxx')
        self.assertEqual('https://api.linkedin.com', api.BASE_URL)
