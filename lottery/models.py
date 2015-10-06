"""This file contains all model definitions for the lottery module

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.3.0
@since: 2015-10-05
"""

from django.db import models
from django.contrib.auth.models import User


class Lottery(models.Model):
    title = models.CharField(max_length=140, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    winner = models.OneToOneField(User, blank=True,
                                  related_name='lottery_winner',
                                  null=True, on_delete=models.SET_NULL)
    max_entries = models.PositiveIntegerField()
    entries = models.ManyToManyField(User, through='Entry')
    open_entries = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        """Custom save method to generate the entries upon creation"""
        if not self.id:
            super(Lottery, self).save(*args, **kwargs)
            entries = []
            for entry in range(self.max_entries):
                entries.append(Entry(lottery=self))
            Entry.objects.bulk_create(entries)
            self.open_entries = self.max_entries
            winning_entry = Entry.objects.filter(lottery=self
                                                 ).order_by('?').first()
            winning_entry.winner = True
            winning_entry.save()
        super(Lottery, self).save(*args, **kwargs)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return "Lottery %s %s" % (self.start_date, self.start_time)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('lottery-detail', kwargs={"slug": self.slug, })


class Entry(models.Model):
    """Intermediary model for lottery entries with winner, where False equals
    a loosing entry and True equals a winning entry
    """
    lottery = models.ForeignKey('Lottery')
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.SET_NULL)
    winner = models.BooleanField(default=False)
