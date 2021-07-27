from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    """
    расширение страндартной формы регистрации, добавляем
    - first_name
    - last_name
    """
    first_name = forms.CharField(max_length=30, required=False, help_text = 'Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text = 'Фамилия')
    city = forms.CharField(max_length=30, required=False, help_text='Город')
    date_of_birth = forms.DateField(required=True, help_text='День рождения')
    
    
    class Meta():
        """
        Отображаем поля для form
        """
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')