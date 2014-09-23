import unittest
import urllib2

from flask.ext.testing import LiveServerTestCase, TestCase

from tmb import app as tmbapp

class TestTMR(TestCase):

    def create_app(self):
        app = tmbapp
        app.config['TESTING'] = True
        return app

class TestIndex(LiveServerTestCase):

    def create_app(self):
        app = tmbapp
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        return app

    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()
