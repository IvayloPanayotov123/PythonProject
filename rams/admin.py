from django.contrib import admin
from .models import RAM

@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    list_display = ("name", "speed", "gigabytes", "score")
    search_fields = ("name",)
    list_filter = ("gigabytes",)
    ordering = ("name",)
