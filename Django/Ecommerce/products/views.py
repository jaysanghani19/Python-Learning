from django.shortcuts import render

from products.models import Product
from products.forms import ProductForm,RawForm
# Create your views here.
def product_page(request,*args, **kwargs):
    obj = Product.objects.get(id=1)
    data = {
        "object":obj
    }
    return render(request,'product/detail.html',data)

# def create_product(request,*args, **kwargs):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context={
#         "form":form
#     }
#     return render(request,"product/product_create.html",context)

def create_product(request,*args, **kwargs):
    form = RawForm()
    if request.method =='POST':
        form = RawForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
    if form.is_valid():
        form = ProductForm()
    context={
        "form":form
    }
    return render(request,"product/product_create.html",context)