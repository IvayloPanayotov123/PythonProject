from django.urls import path
from orders.views import OrderDeleteView, OrderListView, OrderConfirmView, OrderDeliveredView

app_name = "orders"

urlpatterns = [
    path("<int:pk>/delete/", OrderDeleteView.as_view(), name="delete"),
    path("list/", OrderListView.as_view(), name="list"),
	path("<int:pk>/confirm/", OrderConfirmView.as_view(), name="confirm"),
	path("<int:pk>/delivered/", OrderDeliveredView.as_view(), name="delivered"),
]