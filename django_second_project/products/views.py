from django.shortcuts import render

# Create your views here.

from .models import Product

from .forms import ProductForm

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    context = {'form':form}
    return render(request, "products/create.html", context)

def product_datail(request):
    obj = Product.objects.get(id = 1)
    context = {
        'title':obj.title,
        'description':obj.description
    }
    return render(request, "products/detail.html", context)