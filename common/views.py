from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from rams.models import RAM
from gpus.models import GPU
from cpus.models import CPU

class IndexView(TemplateView):
    template_name = "index.html"

class PartsListView(TemplateView):
    template_name = 'parts/listparts.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['rams'] = RAM.objects.all().order_by('-score', '-speed', '-gigabytes', 'name')
        ctx['gpus'] = GPU.objects.all().order_by('-score', '-vram', 'name')
        ctx['cpus'] = CPU.objects.all().order_by('-score', '-cores', 'name')
        return ctx


class PartsManageView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    pass