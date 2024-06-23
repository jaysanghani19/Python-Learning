from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request,*args, **kwargs):
    return render(request,'home.html',{})

def contact_page(request,*args, **kwargs):
    return render(request,'contact.html',{})


def aboutus_page(request,*args, **kwargs):
    return render(request,'about.html',{})


def product_page(request,*args, **kwargs):
    return render(request,'product.html',{})