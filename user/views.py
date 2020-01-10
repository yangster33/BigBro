from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import View, ListView, DetailView

from .forms import MyLoginForm
from .models import MyUser

# Create your views here.
class MyLogin(LoginView):
    template_name = 'auth_login.html'
    form_class = MyLoginForm


class MyLogout(LogoutView):
    template_name = 'auth_logout.html'

class TestView(ListView):
    model = MyUser
    template_name = 'test.html'

    def get_context_data(self, **kargs):

        context = super().get_context_data(**kargs)
        # print(context)
        return context
