from django.conf.urls import url
from .views import LotteryDetailView, LotteryListView

urlpatterns = [
    url(r'^list/', LotteryListView.as_view(), name="lottery-list"),
    url(r'^(?P<slug>[-\w]+)/', LotteryDetailView.as_view(),
        name="lottery-detail"),
]
