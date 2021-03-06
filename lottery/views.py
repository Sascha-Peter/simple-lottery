"""This file contains all lottery and entry related views.

author: Sascha Peter <sascha.o.peter@gmail.com>
version: 0.4.0
since: 2015-10-05
"""
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import Lottery, Entry


class LotteryListView(ListView):
    """Lottery list view."""

    model = Lottery

    def get_queryset(self):
        """Custom queryset to exclude full or expired lotteries."""
        return Lottery.objects.filter(Q(open_entries__gt=0),
                                      Q(start_date__lte=timezone.now()),
                                      Q(end_date__gte=timezone.now()))


class LotteryDetailView(DetailView):
    """Lottery detail view."""

    model = Lottery

    def get_context_data(self, **kwargs):
        """Get context data and add custom data."""
        context = super(LotteryDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            if self.object.entry_set.filter(user=self.request.user.id):
                context['lottery_entered'] = True
            else:
                context['lottery_entered'] = False
        return context

    def post(self, request, *args, **kwargs):
        """Overwrite post function and add winner to entry."""
        self.object = self.get_object()
        entry = Entry.objects.filter(lottery=self.object.id, user=None
                                     ).order_by('?').first()
        entry.user = request.user
        entry.lottery.open_entries -= 1
        entry.lottery.save()
        entry.save()
        if entry.winner:
            entry.lottery.winner = request.user
            entry.lottery.save()
            entry.save()

        return HttpResponseRedirect(reverse('lottery-detail',
                                            args=[self.object.slug]))
