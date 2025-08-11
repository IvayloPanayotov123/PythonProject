from django.urls import path
from .views import CPUCreateView, delete_cpu, CPUUpdateView

app_name = "cpus"

urlpatterns = [
    path("create/", CPUCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", delete_cpu, name="delete"),
    path('<int:pk>/edit/', CPUUpdateView.as_view(), name='edit'),
]