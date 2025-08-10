from django.contrib import admin
from .models import GPU

@admin.register(GPU)
class GPUAdmin(admin.ModelAdmin):
    list_display = ("name", "vram", "score")
    search_fields = ("name",)
    list_filter = ("vram",)
    ordering = ("name",)
