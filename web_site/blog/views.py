from django.shortcuts import render
from django.http import HttpResponse


posts = [
         {'id':1, 'title': 'Post 1', 'content': 'Content of Post 1'},
         {'id':2, 'title': 'Post 2', 'content': 'Content of Post 2'},
         {'id':3, 'title': 'Post 3', 'content': 'Content of Post 3'},
         {'id':4, 'title': 'Post 4', 'content': 'Content of Post 4'}]

def index(request):

    return render(request,"index.html",{'posts':posts})

def detail(request,id):
    post=None
    for i in posts:
        if i["id"]==id:
            post=i
    return render(request,"detail.html",{'post':post})

def contact(request):
    return render(request,"contact.html")

# Create your views here.
