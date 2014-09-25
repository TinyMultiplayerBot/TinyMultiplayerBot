import unittest
import urllib2

from flask.ext.testing import LiveServerTestCase, TestCase

from tmb import app as tmbapp, db
from tmb.models import User

class TestTMB(TestCase):

    def setUp(self):
        db.create_all()
        super(TestCase, self).setUp()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        super(TestCase, self).tearDown()

    def create_app(self):
        app = tmbapp
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../test.db"
        return app

    def test_create_account(self):
        steamid = "au9a0ou9ea0"

        # There should only be one user
        u = User.get_or_create(steamid)
        db.session.commit()
        user_count = User.query.count()
        self.assertEqual(user_count, 1)

        # There should only be one user
        u2 = User.get_or_create(steamid)
        db.session.commit()
        user_count2 = User.query.count()
        self.assertEqual(user_count2, 1)

        # Now there should be 2 users
        u3 = User.get_or_create("ah9oe0uh")
        db.session.commit()
        user_count3 = User.query.count()
        self.assertEqual(user_count3, 2)


if __name__ == '__main__':
    unittest.main()
