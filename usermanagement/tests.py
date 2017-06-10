"""Unit and functional tests for the user management."""
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
import random
import string


class UserTest(TestCase):
    """Unit tests for testing user related actions."""

    user_password = ''.join(
        random.SystemRandom().choice(
            string.ascii_uppercase + string.digits
        ) for _ in range(16)
    )

    def setUp(self):
        """Define test users and factories."""
        self.client = Client()
        self.factory = RequestFactory()
        self.user_one = User.objects.create_user(
            username="dummy", email="dummy@test.com",
            password="dummy_password")
        self.user_anonymous = AnonymousUser()

    def test_homepage(self):
        """Test if the homepage is available and working."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        """Test if the login process is working for a defined user."""
        test_user = self.client.login(username='dummy',
                                      password=self.user_one.password)
        self.assertEqual(test_user, True)
