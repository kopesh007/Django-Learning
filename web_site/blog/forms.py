from django import forms


class contactform(forms.Form):
    name = forms.CharField(label='name',max_length=100,required=True)
    email = forms.EmailField(label='email',required=True)
    message = forms.CharField(label='mess',max_length=500,required=True)