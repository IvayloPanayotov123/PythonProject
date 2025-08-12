from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Create two staff users (Trayan→Suppliers, Nikola→Merchants) and add them to the groups. Only username existence is checked."

    def handle(self, *args, **options):
        User = get_user_model()

        def add_user(username, first_name, email, password, group_name):
            try:
                group = Group.objects.get(name=group_name)
            except Group.DoesNotExist:
                raise CommandError(f"Group '{group_name}' does not exist.")

            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    "first_name": first_name,
                    "email": email,
                    "is_staff": True,
                    "is_superuser": False,
                    "is_active": True,
                    "last_name": "",
                    "address": "",
                    "phone_number": "",
                },
            )

            if created:
                user.set_password(password)
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Created user '{username}'"))
            else:
                if not user.is_staff:
                    user.is_staff = True
                    user.save()
                self.stdout.write(self.style.WARNING(f"User '{username}' already exists; added to group if needed."))

            user.groups.add(group)

        add_user("Trayan", "Trayan", "trayan@trayan.com", "ManThe21st", "Suppliers")
        add_user("Nikola", "Nikola", "nikola@nikola.com", "ManThe21st", "Merchants")
        self.stdout.write(self.style.SUCCESS("Done."))