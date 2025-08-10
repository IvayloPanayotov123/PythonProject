from django.urls import path
from common import views
from common.views import PartsListView, PartsManageView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('parts/', PartsListView.as_view(), name='parts_list'),
    path('parts/manage/', PartsManageView.as_view(), name='parts_manage'),
]