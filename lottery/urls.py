from django.conf.urls import url
from .views import LotteryDetailView, LotteryListView

urlpatterns = [
    url(r'^list/', LotteryListView.as_view(), name="lottery-list"),
    url(r'^(?P<slug>[-\w]+)/', LotteryDetailView.as_view(),
        name="lottery-detail"),
    url(r'^(?P<slug>[-\w]+)/enter/', 'lottery.views.enter_lottery',
        name="enter-lottery"),
]
