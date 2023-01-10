from django.shortcuts import render,HttpResponseRedirect
from .forms import Signup,Blogform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .models import Blog
from django.contrib.auth.models import User

# Create your views here.

def aboutus(request):
    return render(request , 'aboutus.html')

def home(request):
    forms =Blog.objects.all()
    return render(request , 'home.html',{"form":forms})

def contactus(request):

    return render(request, 'contactus.html')

def dashboard(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            data = Blogform(request.POST , request.FILES)
            if data.is_valid():
                data.save()
                return HttpResponseRedirect('/home/')

        else:
            data = Blogform()
        return render(request, 'dashboard.html',{'form':data})
    else:
        return HttpResponseRedirect('/loginpage/')

def signuppage(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = Signup(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/login/')
        else:    
            form = Signup()
        return render(request , 'signup.html' , {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def loginpage(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = AuthenticationForm(request = request,data=request.POST)
            if form.is_valid():
                username= form.cleaned_data['username']
                password= form.cleaned_data['password']
                user = authenticate(username = username , password = password)
                if user!=None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')

        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


def logoutpage(request):
    logout(request)
    return render(request, 'home.html')