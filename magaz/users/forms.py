from django import forms
from .models import Person
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            "username": forms.TextInput(attrs={
                'placeholder': 'Имя'
            }),
            "email": forms.TextInput(attrs={
                'placeholder': 'Почта'
            }),

        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))
    pasrepeat = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль'
    }))

    class Meta:
        model = Person
        fields = ['name', 'email', 'age', 'gender']

        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "email": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
            "age": forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),

        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя'
    }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))
