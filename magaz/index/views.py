from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    return render(request, "index.html")
def news(request):
    return render(request, "news.html")
def contact(request):
    return render(request, "contacts.html")
def user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}, твоя почта: {email}</h2>")
    else:
        userform = UserForm()
        return render(request, "user.html", {"form": userform})
# Create your views here.
