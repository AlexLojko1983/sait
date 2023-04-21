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
# def user(request):
#     users = Person.objects.order_by('-date')
#     return render(request, 'user.html', {'form': users})
def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"index.html")
        else:
            HttpResponse('INVALID DATA')
    userform = UserForm()

    return render(request, 'user.html', {'form': userform})


# Create your views here.
