from django.urls import path
from .views import CPUCreateView, delete_cpu

app_name = "cpus"

urlpatterns = [
    path("create/", CPUCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", delete_cpu, name="delete"),
]