from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.password_validation import validate_password

from accounts.models import AppUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=20, required=True)

    class Meta:
        model = AppUser
        fields = ['username', 'email', 'first_name', 'last_name', 'address', 'phone_number', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class QuickPasswordForm(forms.Form):
    new_password = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"placeholder": "New password"}),
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean_new_password(self):
        pasword = self.cleaned_data["new_password"]
        validate_password(pasword, self.user)
        return pasword

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ["first_name", "last_name", "address", "phone_number"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name"}),
            "address": forms.TextInput(attrs={"placeholder": "Address"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "Phone number"}),
        }