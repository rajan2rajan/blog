from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Signup(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput,required=True)
    first_name = forms.CharField(required=True)
    password2 = forms.CharField(widget=forms.PasswordInput,label='confirm password')
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}

# R9865177862