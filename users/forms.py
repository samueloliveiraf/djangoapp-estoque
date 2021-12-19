from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Informe um e-mail válido')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )