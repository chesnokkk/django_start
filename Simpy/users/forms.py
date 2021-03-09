from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Введите email', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Введите логин', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        )
    password2 = forms.CharField(
        label='Повторите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control'})
        )

    class Meta:
        model = User
        fields = ['email', 'username','password1', 'password2']
