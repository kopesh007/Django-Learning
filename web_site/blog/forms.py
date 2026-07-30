from django import forms
from django.contrib.auth.models import User


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