from django.contrib import admin
from .models import CPU

@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    list_display = ("name", "cores", "score")
    search_fields = ("name",)
    list_filter = ("cores",)
    ordering = ("name",)