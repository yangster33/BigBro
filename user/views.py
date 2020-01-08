from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from .forms import MyLoginForm

# Create your views here.
class MyLogin(LoginView):
    template_name = 'login.html'
    form_class = MyLoginForm


class MylLogout(LogoutView):
    template_name = 'logout.html'