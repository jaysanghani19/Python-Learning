from django.shortcuts import render, get_object_or_404,redirect

from products.models import Product
from products.forms import ProductForm
# Create your views here.
def product_page(request,*args, **kwargs):
    obj = Product.objects.all()
    data = {
        "object":obj
    }
    return render(request,'product/products.html',data)

def create_product(request,*args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/products')
        # form = ProductForm()
    context={
        "form":form
    }
    return render(request,"product/product_create.html",context)


def update_product(request,id):
    obj = Product.objects.get(id=id)
    form = ProductForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/products')
    context={
        "form":form
    }
    return render(request,"product/product_create.html",context)

def dyanmic_product(request,id,*args, **kwargs):
    obj = get_object_or_404(Product, id=id)
    data = {
        'object': obj
    }
    return render(request,'product/detail.html',data)