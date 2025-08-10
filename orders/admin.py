from django.contrib import admin
from orders.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "pc", "confirmed", "delivered")
    list_filter = ("confirmed", "delivered")
    search_fields = ("user__username", "pc__name")
    ordering = ("-id",)
    actions = ["mark_confirmed", "mark_delivered"]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm("orders.can_confirm_orders"):
            actions.pop("mark_confirmed", None)
        if not request.user.has_perm("orders.can_mark_delivered"):
            actions.pop("mark_delivered", None)
        return actions

    def mark_confirmed(self, request, queryset):
        if not request.user.has_perm("orders.can_confirm_orders"):
            self.message_user(request, "You don't have permission to confirm orders.", level='error')
            return
        updated = queryset.update(confirmed=True)
        self.message_user(request, f"{updated} order(s) marked as confirmed.")
    mark_confirmed.short_description = "Mark selected orders as confirmed"

    def mark_delivered(self, request, queryset):
        if not request.user.has_perm("orders.can_mark_delivered"):
            self.message_user(request, "You don't have permission to mark delivered.", level='error')
            return
        updated = queryset.update(delivered=True)
        self.message_user(request, f"{updated} order(s) marked as delivered.")
    mark_delivered.short_description = "Mark selected orders as delivered"