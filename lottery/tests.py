"""This file contains all lottery related test cases

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.3.0
@since: 2015-10-06
"""
from django.test import Client, TestCase, RequestFactory
from django.core.urlresolvers import reverse

from .models import Lottery

import datetime


class LotteryTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.time_in_3 = datetime.datetime.now() + datetime.timedelta(hours=3)

    def test_list_view(self):
        """Tests the lottery list view"""
        response = self.client.get(reverse('lottery-list'))
        self.assertEqual(response.status_code, 200)
