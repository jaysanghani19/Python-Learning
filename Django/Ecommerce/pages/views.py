from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request,*args, **kwargs):
    context ={
        "name" : "Jay",
        "age" : 20
    }
    return render(request,'home.html',context)

def contact_page(request,*args, **kwargs):
    return render(request,'contact.html',{})


def aboutus_page(request,*args, **kwargs):
    return render(request,'about.html',{})


