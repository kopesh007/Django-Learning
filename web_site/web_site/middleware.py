from django.urls import reverse
from django.shortcuts import render,redirect


class auth_redirect:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        if request.user.is_authenticated:
            lis_path = [reverse("blog:login"),reverse("blog:register")]
            print(request.path)
            if request.path in lis_path:
                return redirect(reverse("blog:index"))
        res = self.get_response(request)
        return res

# this class for handling unnauthenticate user 
class auth_redirect_un:
    def __init__(self,response):
        self.response = response

    def __call__(self,request):
        if not request.user.is_authenticated:
            lis = [reverse("blog:dash")]
            if( request.path in lis):
                return redirect("blog:index")
        res = self.response(request)
        return res

