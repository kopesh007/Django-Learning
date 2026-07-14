from django.shortcuts import render
from django.http import HttpResponse
from .models import posts





def index(request):
    p=posts.objects.all()

    return render(request,"index.html",{'posts':p})

def detail(request,id):
    post=None
    for i in posts:
        if i["id"]==id:
            post=i
    return render(request,"detail.html",{'post':post})

def contact(request):
    return render(request,"contact.html")

# Create your views here.
