"""This file contains all administrative views for the lottery module

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.4.0
@since: 2015-10-05
"""
from django.contrib import admin
from django.template.response import TemplateResponse

from .models import Lottery, Entry


class EntryInline(admin.StackedInline):
    model = Entry
    extra = 0

    def get_max_num(self, request, obj=None, **kwargs):
        """Custom get_max_num method to limit based on maximum entries"""
        max_num = 5
        if obj:
            max_num = obj.max_entries
            return max_num
        return max_num


class LotteryAdmin(admin.ModelAdmin):
    model = Lottery
    inlines = [EntryInline, ]
    exclude = ('entries', )
    readonly_fields = ('open_entries', )
    list_display = ('title', 'start_date', 'end_date', 'slug', 'winner')
    prepopulated_fields = {"slug": ("title", "start_date", )}


class EntryAdmin(admin.ModelAdmin):
    model = Entry


def show_lottery_winner(request):
    lotteries = Lottery.objects.all()
    context = {}
    context['winners'] = {}

    for lottery in lotteries:
        winner = lottery.entry_set.get(winner=True)
        if winner.user:
            context['winners'][lottery.slug] = winner.user
        else:
            context['winners'][lottery.slug] = "No winner yet!"

    return TemplateResponse(request, "winner_list.html", context)

admin.site.register(Lottery, LotteryAdmin)
admin.site.register(Entry, EntryAdmin)
