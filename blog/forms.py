from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog

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


class Blogform(forms.ModelForm):
    date = forms.DateField(label="publish date",initial = datetime.date.today())
    class Meta:
        model = Blog
        fields =['title','imagefields','describe','date']