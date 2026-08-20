from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import posts,cat


class contactform(forms.Form):
    name = forms.CharField(label='name',max_length=100,required=True)
    email = forms.EmailField(label='email',required=True)
    message = forms.CharField(label='mess',max_length=500,required=True)

class regi(forms.ModelForm):
    username = forms.CharField(label='Name',required=True)
    email = forms.EmailField(label='Email',required=True)
    password = forms.CharField(label='Password',required=True)
    c_password = forms.CharField(label ='Conform Password',required=True)

    class Meta:
        model = User
        fields = ["username","email","password"]
    
    def clean(self):
        cleaned_data = super().clean()
        pas = cleaned_data.get("password")
        c_pas = cleaned_data.get("c_password")
        email = cleaned_data.get("email")
        if(pas and c_pas and pas != c_pas):
            raise forms.ValidationError("Password Mismatch !!!")
        if(User.objects.filter(email=email).exists()):
            raise forms.ValidationError("This Email Already Exists !") # this is known as non field Errors

class log(forms.Form):
    name = forms.CharField(label="Name",max_length=100,required=True)
    password = forms.CharField(label="Password",max_length=100,required=True)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        password = cleaned_data.get("password")
        
        if(name and password):
            user = authenticate(username=name,password=password)
            if(user is None):
                raise forms.ValidationError("Invalid Username and Password !")

class password_form(forms.Form):
    
    email = forms.EmailField(label="Email")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("User Not Registered yett !")

class change_pass(forms.Form):
    password = forms.CharField(label="New Password",max_length=100,required=True)
    c_password = forms.CharField(label="Confirm Password",max_length=100,required=True)

    def clean(self):
        cleaned_data = super().clean()
        p = cleaned_data.get("password")
        c_p = cleaned_data.get("c_password")

        if (p and c_p and (not p == c_p)):
            raise forms.ValidationError("Password Mismatch !!!")

class n_posts(forms.ModelForm):
    title = forms.CharField(max_length=100,required = True,label="Title")
    content = forms.CharField(max_length=100,required=True,label="Content")
    category = forms.ModelChoiceField(label="Category",queryset=cat.objects.all())

    class Meta:
        model = posts
        fields = ['title','content','category']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if (title and len(title)<5):
            raise forms.ValidationError("Title Must Be Larger Than 5 Characters !")
        
        if (content and len(content)<10):
            raise forms.ValidationError("Content Must Be Larger Than 10 Characters !")




        