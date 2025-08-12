from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, ListView

from orders.models import Order


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy("profile")

    def get_queryset(self):
        return Order.objects.select_related("pc").filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        with transaction.atomic():
            pc = self.object.pc
            pc.delete()
        return redirect(self.get_success_url())

    def get(self, request, *args, **kwargs):
        # no confirm page
        return redirect(self.get_success_url())


class MerchantsOnlyMixin(UserPassesTestMixin):
	def test_func(self):
		u = self.request.user
		return u.is_authenticated and u.groups.filter(name="Merchants").exists()

	def handle_no_permission(self):
		return redirect("login")

class OrderListView(LoginRequiredMixin, MerchantsOnlyMixin, ListView):
	model = Order
	template_name = "orders/orderList.html"
	context_object_name = "orders"
	paginate_by = 25

	def get_queryset(self):
		return Order.objects.select_related("pc", "user").order_by("-pk")

class OrderConfirmView(LoginRequiredMixin, PermissionRequiredMixin, View):
	permission_required = "orders.can_confirm_orders"
	raise_exception = False
	success_url = reverse_lazy("orders:list")

	def post(self, request, pk):
		order = get_object_or_404(Order, pk=pk)
		order.confirmed = True
		order.save(update_fields=["confirmed"])
		return redirect(self.success_url)

	def get(self, request, pk):
		return redirect(self.success_url)

class OrderDeliveredView(LoginRequiredMixin, PermissionRequiredMixin, View):
	permission_required = "orders.can_mark_delivered"
	raise_exception = False
	success_url = reverse_lazy("orders:list")

	def post(self, request, pk):
		order = get_object_or_404(Order, pk=pk)
		order.delivered = True
		order.save(update_fields=["delivered"])
		return redirect(self.success_url)

	def get(self, request, pk):
		return redirect(self.success_url)
