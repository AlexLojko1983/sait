from django import forms
from django.forms import ModelForm, TextInput, EmailField, PasswordInput
from .models import Person


class UserForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'age', 'password','gender']

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
            # "gender": forms.CheckboxInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Пол'
            # }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
        }
        # name = forms.CharField(help_text="Введите свое имя")
        # email = forms.EmailField()
        # age = forms.IntegerField(initial=20, required=False)
        # gender = forms.ChoiceField(choices=[("Woman", "W"), ("Man", "M")], initial="Man")
        # password = forms.CharField(widget=forms.PasswordInput())
