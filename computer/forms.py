from django import forms
from .models import Computer

class ComputerCreateForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ["name", "ram", "gpu", "cpu"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name your PC"}),
        }