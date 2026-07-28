from django import forms
from django.contrib.auth.models import User


class contactform(forms.Form):
    name = forms.CharField(label='name',max_length=100,required=True)
    email = forms.EmailField(label='email',required=True)
    message = forms.CharField(label='mess',max_length=500,required=True)

class regi(forms.ModelForm):
    username = forms.CharField(label='name')
    email = forms.EmailField(label='email')
    password = forms.CharField(label='pass')
    c_password = forms.CharField(label ='c_pass')

    class Meta:
        model = User
        fields = ["username","email","password"]