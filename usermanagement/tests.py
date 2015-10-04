from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User, AnonymousUser


class UserTest(TestCase):
    """Unit tests for testing user related actions"""
    def setUp(self):
        """Define test users and factories"""
        self.client = Client()
        self.factory = RequestFactory()
        self.user_one = User.objects.create_user(
            username="dummy", email="dummy@test.com", password="dummypw")
        self.user_anonymous = AnonymousUser()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        test_user = self.client.login(username='dummy', password='dummypw')
        self.assertEqual(test_user, True)
