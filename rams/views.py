from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.http import require_POST
from django.views.generic import CreateView
from .models import RAM
from .forms import RAMForm

def is_marketeer_or_superuser(user):
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name="Marketeers").exists())

class RAMCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = RAM
    form_class = RAMForm
    template_name = "parts/createRAM.html"
    success_url = reverse_lazy("parts_manage")

    def test_func(self):
        return is_marketeer_or_superuser(self.request.user)

@login_required
@user_passes_test(is_marketeer_or_superuser)
@require_POST
def delete_ram(request, pk):
    ram = get_object_or_404(RAM, pk=pk)
    ram.delete()
    return redirect('parts_manage')