from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import password_validation


class MyLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': "form-control", 'placeholder': "用户名"}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': "form-control", 'placeholder': "密码"}),
    )


class MyPasswordChangeForm(PasswordChangeForm):

    error_messages = {
        'password_incorrect': ("原始密码输入错误，请再次输入原始密码。"),
        'password_mismatch': ('两次新密码输入不匹配，请重新输入密码.'),
    }

    old_password = forms.CharField(
        label=("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'autofocus': True, 'class': "form-control", 'placeholder': "旧密码"}),
    )

    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': "form-control", 'placeholder': "新密码"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': "form-control", 'placeholder': "再次输入新密码"}),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']
