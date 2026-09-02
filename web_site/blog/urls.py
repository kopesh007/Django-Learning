from django.urls import path
from .import views

app_name ='blog'

urlpatterns=[
    path("",views.index,name="index"),
    path("detail/<str:sl>/",views.detail,name="detail"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about_f,name="about"),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("dash/",views.dash,name="dash"),
    path("logout/",views.logout,name="logout"),
    path("f_pass/",views.f_pass,name="f_pass"),
    path("reset_pass/<uidb64>/<token>",views.reset_pass_email,name="reset"),
    path("new_post/",views.new_post,name="new_post"),
    path("edit_post/<int:post_id>/",views.edit_post,name="edit_post")
]