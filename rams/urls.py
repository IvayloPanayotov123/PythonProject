from django.urls import path
from .views import RAMCreateView, delete_ram, RAMUpdateView

app_name = "rams"

urlpatterns = [
    path("create/", RAMCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", delete_ram, name="delete"),
    path('<int:pk>/edit/', RAMUpdateView.as_view(), name='edit'),
]