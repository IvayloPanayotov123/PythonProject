from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm, LoginForm, QuickPasswordForm, ProfileEditForm
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

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account_data/profile.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["orders"] = self.request.user.orders.select_related("pc").order_by("-pk")
        ctx["pw_form"] = QuickPasswordForm(user=self.request.user)  # <- needed
        return ctx

    def post(self, request, *args, **kwargs):
        if request.POST.get("action") == "change_password":
            form = QuickPasswordForm(request.POST, user=request.user)
            if form.is_valid():
                user = request.user
                user.set_password(form.cleaned_data["new_password"])
                user.save()
                update_session_auth_hash(request, user)
                return redirect("profile")
            ctx = self.get_context_data()
            ctx["pw_form"] = form
            return self.render_to_response(ctx)
        return self.get(request, *args, **kwargs)

class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = ProfileEditForm
    template_name = "account_data/editProfile.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user
