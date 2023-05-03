from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


def addProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProductForm()
    return render(request, 'products/register.html', {'form': form})

def index(request):
    product = Product.objects.all()
    return render(request, "base.html", {'product': product})



# Create your views here.
