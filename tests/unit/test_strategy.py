from unittest import mock

from masonite.testing import TestCase

from socialite.helpers import load_strategy, load_backend


class TestMasoniteStrategy(TestCase):

    def setUp(self):
        super(TestMasoniteStrategy, self).setUp()
        self.request = self.get('/', params={'x': 1}).request
        self.strategy = load_strategy(request=self.request)

    def test_request_methods(self):
        self.assertEqual(self.strategy.request_port(), '8000')
        self.assertEqual(self.strategy.request_path(), '/')
        self.assertEqual(self.strategy.request_host(), 'http://testserver')
        self.assertEqual(self.strategy.request_is_secure(), False)
        self.assertEqual(self.strategy.request_data(), self.request.all())
        self.assertEqual(self.strategy.request_get(), self.request.all())
        self.assertEqual(self.strategy.request_post(), self.request.all())
        self.request.method = 'POST'
        self.assertEqual(self.strategy.request_data(merge=False), {})

    def test_get_setting(self):
        self.assertEqual(self.strategy.get_setting("SOCIAL_AUTH_FACEBOOK_KEY"), 1)
        self.assertEqual(self.strategy.get_setting("SOCIAL_AUTH_FACEBOOK_SECRET"), 2)

    def test_html(self):
        self.assertEqual(self.strategy.render_html(tpl='test.html'), 'test')

        self.assertEqual(self.strategy.render_html(html='test'), b'test')

        self.assertEqual(self.strategy.html(content='test'), b'test')

    def test_sessions(self):
        self.strategy.session_set('k', 'v')
        self.assertEqual(self.strategy.session_get('k'), 'v')
        self.assertEqual(self.strategy.session_set('k', 'x'), 'x')
        self.strategy.session_pop('k')
        self.assertEqual(self.strategy.session_get('k'), None)

    def test_build_absolute_uri(self):
        self.assertEqual(self.strategy.build_absolute_uri('/'), 'http://testserver/')

    def test_authenticate(self):
        backend = load_backend(strategy=self.strategy, name='facebook',
                               redirect_uri='/')
        self.assertEqual(backend.name, 'facebook')

        user = mock.Mock()
        with mock.patch('socialite.strategy.MasoniteStrategy.authenticate', return_value=user):
            result = self.strategy.authenticate(backend=backend, response=user)
            self.assertEqual(result, user)
