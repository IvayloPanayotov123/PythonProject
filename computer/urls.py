from django.urls import path
from .views import ComputerCreateView

app_name = "computer"

urlpatterns = [
    path("create/", ComputerCreateView.as_view(), name="create"),
]