from django import template

register = template.Library()

@register.filter
def is_marketeer(user):
    return user.is_authenticated and user.groups.filter(name="Marketeers").exists()

@register.filter
def is_superuser_or_marketeer(user):
    return (
        user.is_authenticated and (
            user.is_superuser or user.groups.filter(name="Marketeers").exists()
        )
    )