from django.shortcuts import render
from django.http import HttpResponse
from .models import posts
from django.core.paginator import Paginator
from .forms import contactform





def index(request):
    all_posts = posts.objects.all().order_by("title")
    all_pages = Paginator(all_posts,5)
    pg = request.GET.get('page')
    pg_posts = all_pages.get_page(pg)


    return render(request,"index.html",{'posts':pg_posts})

def detail(request,sl):
    try:
        post=posts.objects.get(slug=sl)
        rel=posts.objects.filter(cato=post.cato).exclude(slug=sl)
    except Exception :
        post=None
    return render(request,"detail.html",{'post':post,'related':rel})



def contact(request):
    
    form = contactform()
    if(request.method == "POST"):
        form = contactform(request.POST)
        name = request.POST["name"]
        email = request.POST["email"]
        mess = request.POST["message"]
        if form.is_valid():
            print(form.cleaned_data["name"])
        else:
            return render(request,"contact.html",{'form':form,'name':name,'email':email,'mess':mess})
        
    return render(request,"contact.html")

# Create your views here.
