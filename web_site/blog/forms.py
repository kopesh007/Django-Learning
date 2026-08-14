from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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
        if(pas and c_pas and pas != c_pas):
            raise forms.ValidationError("Password Mismatch !!!") # this is known as non field Errors

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

        