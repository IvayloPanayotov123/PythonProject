from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import AppUser

@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "address", "phone_number", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "email", "first_name", "last_name", "address", "phone_number")
    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "address", "phone_number")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "address", "phone_number", "password1", "password2"),
        }),
    )

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return [f.name for f in self.model._meta.fields] + [
                "groups", "user_permissions"
            ]
        return super().get_readonly_fields(request, obj)