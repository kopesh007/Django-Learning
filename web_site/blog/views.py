from django.shortcuts import render
from django.http import HttpResponse
from .models import posts





def index(request):
    p=posts.objects.all().order_by("-title")

    return render(request,"index.html",{'posts':p})

def detail(request,id):
    try:
        post=posts.objects.get(pk=id)
    except Exception :
        post=None
    return render(request,"detail.html",{'post':post})

def contact(request):
    return render(request,"contact.html")

# Create your views here.
