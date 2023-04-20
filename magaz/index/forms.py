from django import forms
from django.forms import ModelForm, TextInput, EmailField, IntegerField, PasswordInput
from .models import Person


class UserForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'age', 'password']
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "email": EmailField(),
            "age": IntegerField(),
            "password": PasswordInput(),
        }
        # name = forms.CharField(help_text="Введите свое имя")
        # email = forms.EmailField()
        # age = forms.IntegerField(initial=20, required=False)
        # gender = forms.ChoiceField(choices=[("Woman", "W"), ("Man", "M")], initial="Man")
        # password = forms.CharField(widget=forms.PasswordInput())
