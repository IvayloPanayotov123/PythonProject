from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

class RAM(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(5)])
    speed = models.IntegerField(validators=[MinValueValidator(1)])  # MHz
    score = models.IntegerField(validators=[MinValueValidator(100)])
    gigabytes = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name