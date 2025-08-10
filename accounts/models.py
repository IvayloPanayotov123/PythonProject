from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username