from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import Person
import asyncio


def index(request):
    return render(request, "index.html")
def news(request):
    return render(request, "news.html")
def contact(request):
    return render(request, "contacts.html")
def user(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            age = userform.cleaned_data["age"]
            email = userform.cleaned_data["email"]
            # gender = userform.cleaned_data["gender"]
            password = userform.cleaned_data["password"]
            # userform.save()
            return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}, твоя почта: {email}</h2>, <h1>Pas: {password}</h1>")
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()
        return render(request, "user.html", {"form": userform})


# Create your views here.
