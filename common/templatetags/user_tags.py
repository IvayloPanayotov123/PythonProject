from django import template

register = template.Library()

@register.filter
def is_marketeer(user):
	return user.is_authenticated and user.groups.filter(name="Suppliers").exists()

@register.filter
def is_superuser_or_marketeer(user):
	return (
		user.is_authenticated and (
			user.is_superuser or user.groups.filter(name="Suppliers").exists()
		)
	)

@register.filter(name="is_merchant")
def is_merchant(user):
	if not getattr(user, "is_authenticated", False):
		return False
	return user.groups.filter(name="Merchants").exists()