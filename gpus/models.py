from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

class GPU(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(5)])
    vram = models.IntegerField(validators=[MinValueValidator(1)])  # GB
    score = models.IntegerField(validators=[MinValueValidator(100)])

    def __str__(self):
        return self.name