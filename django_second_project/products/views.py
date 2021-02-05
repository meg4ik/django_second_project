from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
# Create your views here.

from .models import Product

from .forms import ProductForm

def product_delete(request,eid):
    if request.method == "POST":
        try:
            obj = get_object_or_404(Product, id = eid)
        except Product.DoesNotExist as e:
            raise e
        else:
            obj.delete()
            return redirect('../../')
    else:
        return render(request, "products/delete.html")

def dynamic_lookup(request, eid):
    if request.method == "GET":
        try:
            obj = get_object_or_404(Product, id = eid)
        except Product.DoesNotExist:
            raise Http404
        else:
            content = {
                'obj':obj
            }
            return render(request, "products/detail.html", content)

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        initial_data = {
            'title':"Enter your title"
        }
        form = ProductForm(initial=initial_data)
    context = {'form':form}
    return render(request, "products/create.html", context)