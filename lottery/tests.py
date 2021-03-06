"""This file contains all lottery related test cases.

author: Sascha Peter <sascha.o.peter@gmail.com>
version: 0.4.0
since: 2015-10-06
"""
from django.test import Client, TestCase, RequestFactory
from django.core.urlresolvers import reverse

import datetime


class LotteryTest(TestCase):
    """Lottery test cases."""

    def setUp(self):
        """Test setup."""
        self.factory = RequestFactory()
        self.client = Client()
        self.time_in_3 = datetime.datetime.now() + datetime.timedelta(hours=3)

    def test_list_view(self):
        """Test the lottery list view."""
        response = self.client.get(reverse('lottery-list'))
        self.assertEqual(response.status_code, 200)
