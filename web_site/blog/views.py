from django.shortcuts import render
from django.http import HttpResponse
from .models import posts,about,user_data
from django.core.paginator import Paginator
from .forms import contactform,regi
from django.contrib import messages





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
            msg="Data Has Been Submitted , Team Will Reach You !"
            user_data.objects.create(name=name,email=email,message=mess)
            return render(request,"contact.html",{'form':form,'msg':msg})
        else:
            return render(request,"contact.html",{'form':form,'name':name,'email':email,'mess':mess})
        
    return render(request,"contact.html")

def about_f(request):
    
    con = about.objects.first()
    if (con is None or not con.content):
        con="Empty"
    return render(request,"about.html",{'con':con})

def register(request):
    form = regi()
    if(request.method == "POST"):
        form = regi(request.POST)
        name = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        c_password = request.POST["c_password"]
        if(form.is_valid()):
            user=form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request,"Registered ! , Now you can login")
        else:
            return render(request,"register.html",{'name':name,'email':email,'passw':password,'c_pass':c_password,'form':form})
    return render(request,"register.html",{'form':form})

# Create your views here.
