from unittest import mock

from masonite.testing import TestCase


class TestSocialiteController(TestCase):

    def test_begin_view(self):
        self.get(f"/social/facebook/login").assertIsStatus(302)

        # self.get(f"/{SOCIAL_AUTH_NAMESPACE}/google/login").assertIsStatus(500)

    @mock.patch('social_core.backends.base.BaseAuth.request')
    def test_complete(self, mock_request):
        # self.get(f"/{SOCIAL_AUTH_NAMESPACE}/facebook/callback?code=1").assertIsStatus(200)
        pass
