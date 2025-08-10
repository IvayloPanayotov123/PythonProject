from django import forms
from .models import CPU

class CPUForm(forms.ModelForm):
    class Meta:
        model = CPU
        fields = ['name', 'cores', 'score']