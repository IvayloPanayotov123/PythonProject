from django.contrib import admin
from .models import Computer

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ("name", "creator", "cpu", "gpu", "ram", "price")
    search_fields = ("name", "creator__username", "cpu__name", "gpu__name", "ram__name")
    list_filter = ("creator",)
    readonly_fields = ("price",)
    ordering = ("name",)