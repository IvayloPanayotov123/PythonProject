from django.urls import path
from .views import ComputerCreateView, ComputerUpdateView

app_name = "computer"

urlpatterns = [
    path("create/", ComputerCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", ComputerUpdateView.as_view(), name="edit"),
]