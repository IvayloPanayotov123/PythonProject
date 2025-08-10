from django import forms
from .models import RAM

class RAMForm(forms.ModelForm):
    class Meta:
        model = RAM
        fields = ["name", "speed", "gigabytes", "score"]