from decimal import Decimal
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from computer.models import Computer
from computer.forms import ComputerCreateForm, ComputerEditForm
from orders.models import Order

class ComputerCreateView(LoginRequiredMixin, CreateView):
    model = Computer
    form_class = ComputerCreateForm
    template_name = "pc/createPC.html"
    success_url = reverse_lazy("index")

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()

        if "preview" in request.POST:
            if form.is_valid():
                ram = form.cleaned_data["ram"]
                gpu = form.cleaned_data["gpu"]
                cpu = form.cleaned_data["cpu"]
                price = (ram.score + gpu.score + cpu.score) * Decimal("1.2")
                context = self.get_context_data(form=form, preview_price=price)
                return self.render_to_response(context)
            return self.form_invalid(form)

        if form.is_valid():
            form.instance.creator = request.user
            response = super().form_valid(form)
            Order.objects.create(user=request.user, pc=self.object)
            return response
        return self.form_invalid(form)

class ComputerUpdateView(LoginRequiredMixin, UpdateView):
    model = Computer
    form_class = ComputerEditForm
    template_name = "pc/editPC.html"
    success_url = reverse_lazy("profile")

    def get_queryset(self):
        return Computer.objects.filter(creator=self.request.user)