from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from typing import Iterable, List


def perms_for(model, actions: Iterable[str]) -> List[Permission]:
	ct = ContentType.objects.get_for_model(model)
	codenames = [f"{a}_{model._meta.model_name}" for a in actions]
	return list(Permission.objects.filter(content_type=ct, codename__in=codenames))


class Command(BaseCommand):
	help = "Create/refresh Suppliers and Merchants groups with the required permissions."

	def handle(self, *args, **options):
		AppUser = apps.get_model("accounts", "AppUser")
		Order = apps.get_model("orders", "Order")
		RAM = apps.get_model("rams", "RAM")
		GPU = apps.get_model("gpus", "GPU")
		CPU = apps.get_model("cpus", "CPU")

		suppliers_group, _ = Group.objects.get_or_create(name="Suppliers")
		merchants_group, _ = Group.objects.get_or_create(name="Merchants")

		suppliers_perms = []
		for model in (RAM, GPU, CPU):
			suppliers_perms += perms_for(model, ["add", "change", "delete", "view"])
		suppliers_perms += perms_for(AppUser, ["view"])
		suppliers_perms += perms_for(Order, ["view"])

		# Merchants:
		order_ct = ContentType.objects.get_for_model(Order)
		merchants_perms = list(
			Permission.objects.filter(
				content_type=order_ct,
				codename__in=["can_confirm_orders", "can_mark_delivered"],
			)
		)

		suppliers_group.permissions.set(suppliers_perms)
		merchants_group.permissions.set(merchants_perms)

		self.stdout.write(self.style.SUCCESS("Groups ensured: Suppliers, Merchants"))
		self.stdout.write(
			self.style.SUCCESS(
				f"Suppliers perms: {', '.join(sorted(p.codename for p in suppliers_perms))}"
			)
		)
		self.stdout.write(
			self.style.SUCCESS(
				f"Merchants perms: {', '.join(sorted(p.codename for p in merchants_perms))}"
			)
		)
		self.stdout.write(
			self.style.WARNING(
				"Reminder: users must have is_staff=True to access the admin site."
			)
		)