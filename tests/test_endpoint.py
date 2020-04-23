import unittest
import app
from unittest.mock import MagicMock


class EndpointTests(unittest.TestCase):

    def setUp(self):
        app.relay_get = MagicMock()

    def tearDown(self):
        pass

    # Test for root would give 404 since it is not defined in the app
    def test_home(self):
        app.get('')
        app.relay_get.assert_called_once_with('', app.logger)

    # Test for simple path
    def test_get_restaurant(self):
        app.get('species')
        app.relay_get.assert_called_once_with('species', app.logger)

    # Test for nested path /restaurant/haga
    def test_get_restaurant_haga(self):
        app.get('species/3')
        app.relay_get.assert_called_once_with('species/3', app.logger)

    # Test for any random path
    def test_get_some_uri(self):
        app.get('test')
        app.relay_get.assert_called_once_with('test', app.logger)


if __name__ == '__main__':
    unittest.main()
