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

    def test_list_count(self):
        """Tests if the created lotteries are being displayed"""
        Lottery.objects.create(title="test1", start_date=datetime.date.today(),
                               end_date=datetime.date.today(),
                               start_time=datetime.datetime.now().time(),
                               end_time=self.time_in_3, max_entries=10)
        response = self.client.get(reverse('lottery-list'))
        self.assertEqual(len(response.context['object_list']), 1)
