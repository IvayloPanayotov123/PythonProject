from django.db import models

class Order(models.Model):
    user = models.ForeignKey('accounts.AppUser', on_delete=models.CASCADE, related_name="orders")
    pc = models.OneToOneField('computer.Computer', on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("can_confirm_orders", "Can confirm orders"),
            ("can_mark_delivered", "Can mark orders as delivered"),
        ]

    def __str__(self):
        return f"Order #{self.pk} - {self.pc.name} for {self.user.username}"