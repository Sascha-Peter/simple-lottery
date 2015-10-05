"""This file contains all lottery and entry related views

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.3.0
@since: 2015-10-05
"""
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.db.models import Q
import datetime

from .models import Lottery


class LotteryListView(ListView):
    model = Lottery

    def get_queryset(self):
        """Custom queryset to exclude full or expired lotteries"""
        return Lottery.objects.filter(Q(open_entries__gt=0) &
                                      Q(end_date__gte=timezone.now()) &
                                      Q(end_time__gt=datetime.datetime.now()))


class LotteryDetailView(DetailView):
    model = Lottery
