from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

class CPU(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(5)])
    cores = models.IntegerField(validators=[MinValueValidator(1)])
    score = models.IntegerField(validators=[MinValueValidator(100)])

    def __str__(self):
        return self.name