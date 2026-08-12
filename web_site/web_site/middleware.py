from django.urls import reverse
from django.shortcuts import render,redirect


class auth_redirect:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        if request.user.is_authenticated:
            lis_path = [reverse("blog:login"),reverse("blog:register")]
            if request.path in lis_path:
                return redirect(reverse("blog:index"))
        else:
            lis_path = [reverse("blog:dash")]
            if request.path in lis_path:
                return redirect(reverse("blog:index"))
        res = self.get_response(request)
        return res


