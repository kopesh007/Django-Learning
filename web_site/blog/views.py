from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import posts,about,user_data,cat
from django.core.paginator import Paginator
from .forms import contactform,regi,log,password_form,change_pass,n_posts
from django.contrib import messages
from django.contrib.auth import authenticate,logout as lout ,login as lin
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.models import User




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
            return redirect("blog:login")
        else:
            return render(request,"register.html",{'name':name,'email':email,'passw':password,'c_pass':c_password,'form':form})
    return render(request,"register.html",{'form':form})

def login(request):
    form = log()
    if(request.method == "POST"):
        form = log(request.POST)
        name=request.POST["name"]
        password = request.POST["password"]
        if(form.is_valid()):
            user = authenticate(username=name,password=password)
            if user is not None:
                lin(request,user)
                print("SUCCESS LOGIN BROOOOOOOOOOOOOOOOOOOO")
                return redirect("blog:dash")
        else:
            return render(request,"login.html",{'form':form,'name':name,'password':password})
        
            
    return render(request,"login.html",{'form':form})



def dash(request):

    all_posts = posts.objects.filter(user=request.user).order_by("title")
    all_pages = Paginator(all_posts,6)
    pg_no = request.GET.get("page")
    pg_posts = all_pages.get_page(pg_no)
    print(request.user)


    return render(request,"dash.html",{'posts':pg_posts})

def logout(request):
    lout(request)
    return redirect("blog:index")

def f_pass(request):
    form = password_form()
    if(request.method == "POST"):
        form = password_form(request.POST)
        email = request.POST["email"]
        if form.is_valid():
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            c_site = get_current_site(request)
            Domain = c_site.domain
            subject = "From Django Corperate"
            message = render_to_string("reset_pass_email.html",{'domain':Domain,'uid':uid ,'token':token})
            print(message)
            send_mail(subject,
            message,
            'vvpr7575@gmail.com',
            [email])
            messages.success(request,"Email Has Been Sent ! ")


            


    return render(request,"f_pass.html",{'form':form})

def reset_pass_email(request,uidb64,token):
    form = change_pass()
    if request.method == "POST":
        form = change_pass(request.POST)
        password = request.POST["password"]
        c_password = request.POST["c_password"]
        if form.is_valid():
            try:
                uid = urlsafe_base64_decode(uidb64)
                user = User.objects.get(id=uid)
            except Exception :
                user = None
            if user is not None and default_token_generator.check_token(user,token):
                user.set_password(password)
                user.save()
                messages.success(request,"Password Has Been Changed !")
                return redirect("blog:login")   
            else:
                messages.error(request,"Something went's Wromg , Please try again ! ") 
        return render(request,"reset.html",{'form':form,'password':password,'c_password':c_password})    
    return render(request,"reset.html",{'form':form})

def new_post(request):
    form = n_posts()
    categories = cat.objects.all()
    if request.method == "POST":
        form = n_posts(request.POST,request.FILES)
        title = request.POST["title"]
        content = request.POST["content"]
        category = request.POST["cato"]
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("blog:dash")
        else:
            return render(request,"new_post.html",{'form':form,'title':title,'content':content,'category':category,'categories':categories})
    return render(request,"new_post.html",{'form':form,"categories":categories})

def edit_post(request,post_id):
    category = cat.objects.all()
    post = get_object_or_404(posts,id=post_id)
    form = n_posts()
    if request.method == "POST":
        form = n_posts(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:dash")

    return render(request,"edit.html",{"categories":category,'form':form,'post':post})

def delete_post(request,post_id):
    post = get_object_or_404(posts,id=post_id)
    post.delete()
    messages.success(request,"Post has Been Deleted Successfully !")
    return redirect("blog:dash")
    
# Create your views here.
