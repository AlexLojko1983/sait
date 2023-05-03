from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User, AnonymousUser
from .models import Person
import asyncio
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Hi {username} !!!')

            return redirect('/')
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
                    messages.success(request, f'Hi {user} !!!')
                    return redirect('/')
                else:
                    return HttpResponse('No active!!')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


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
