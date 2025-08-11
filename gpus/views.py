from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView
from .models import GPU
from .forms import GPUForm

def is_marketeer_or_superuser(user):
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name="Marketeers").exists())

class GPUCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = GPU
    form_class = GPUForm
    template_name = "parts/createGPU.html"
    success_url = reverse_lazy("parts_manage")

    def test_func(self):
        return is_marketeer_or_superuser(self.request.user)

@login_required
@user_passes_test(is_marketeer_or_superuser)
@require_POST
def delete_gpu(request, pk):
    gpu = get_object_or_404(GPU, pk=pk)
    gpu.delete()
    return redirect('parts_manage')

class GPUUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GPU
    form_class = GPUForm
    template_name = 'parts\editGPU.html'
    success_url = reverse_lazy('parts_manage')

    def test_func(self):
        u = self.request.user
        return u.is_superuser or u.groups.filter(name='Marketeers').exists()