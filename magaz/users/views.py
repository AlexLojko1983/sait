from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from .models import Person
import asyncio
from django.contrib.auth import authenticate, login


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


# def user(request):
#     users = Person.objects.order_by('-date')
#     return render(request, 'createuser.html', {'form': users})
def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # new_user = form.save(commit=False)
            # new_user.set_password(form.cleaned_data['password'])
            # new_user.save()
            form.save()

            return render(request, "users/index.html")
        else:
            HttpResponse('INVALID DATA')
    userform = UserForm()

    return render(request, 'create/createuser.html', {'form': userform})

# Create your views here.
