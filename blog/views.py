from django.shortcuts import render,HttpResponseRedirect
from .forms import Signup,Blogform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .models import Blog
from django.contrib.auth.models import User
import os

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
        data = Blogform()
        result = Blog.objects.all()
        username = request.user.username
            
        return render(request, 'dashboard.html',{'form':data,'result':result,'username':username})
    else:
        return HttpResponseRedirect('/loginpage/')

def addpost(request):
    username = request.user.username
    if request.method=="POST":
        form = Blogform(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dashboard/")
    else:
        form = Blogform()
    return render(request , 'addpost.html',{"form":form,'username':username})

def signuppage(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = Signup(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/loginpage/')
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

def edit_page(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            data = Blog.objects.get(pk=id)
            form = Blogform(request.POST,request.FILES , instance=data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')

        else:
            data = Blog.objects.get(pk=id)
            form = Blogform(instance=data)
        return render(request, 'edit.html',{'form':form})
    else:
        return HttpResponseRedirect('/loginpage/')

def delete_page(request,id):
    data = Blog.objects.get(pk=id)
    if len(data.imagefields)>0:
        os.remove(data.imagefields.path)
    data.delete()
    return render(request,'dashboard.html')