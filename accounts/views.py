from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm, LoginForm
from .models import AppUser

class UserRegisterView(CreateView):
    model = AppUser
    form_class = RegisterForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

class UserLoginView(LoginView):
    template_name = 'register/login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('index')

    redirect_authenticated_user = True

class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('index'))