from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import AppUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=20, required=True)

    class Meta:
        model = AppUser
        fields = ['username', 'email', 'address', 'phone_number', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)