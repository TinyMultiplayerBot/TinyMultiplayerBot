import unittest
import urllib2

from flask.ext.testing import LiveServerTestCase, TestCase

from tmr import app as tmrapp

class TestIndex(LiveServerTestCase):

    def create_app(self):
        app = tmrapp
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        return app

    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()
