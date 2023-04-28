from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm, UserRegisterForm
from django.contrib import messages
from .models import Person
import asyncio
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username} !!!')
            return render(request, 'users/login.html', {'form': LoginForm(request.POST)})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['name'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "users/index.html")
                else:
                    return HttpResponse('No active!!')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def index(request):
    return render(request, "base.html")


def news(request):
    return render(request, "news.html")


def contact(request):
    return render(request, "contacts.html")


def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "users/index.html")
        else:
            HttpResponse('INVALID DATA')
    form = UserForm()
    return render(request, 'create/createuser.html', {'form': form})

# Create your views here.
