from django.urls import path
from .views import GPUCreateView, delete_gpu

app_name = "gpus"

urlpatterns = [
    path("create/", GPUCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", delete_gpu, name="delete"),
]