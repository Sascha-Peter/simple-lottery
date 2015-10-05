"""This file contains all administrative views for the lottery module

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.3.0
@since: 2015-10-05
"""
from django.contrib import admin

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
    prepopulated_fields = {"slug": ("title", "start_date", )}


class EntryAdmin(admin.ModelAdmin):
    model = Entry

admin.site.register(Lottery, LotteryAdmin)
admin.site.register(Entry, EntryAdmin)
