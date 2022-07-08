import email
from multiprocessing import context
from urllib import response
from django.forms import PasswordInput
from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from setuptools import find_namespace_packages
import json
from django.contrib.auth.models import User
from . models import UserProfile,Gallery
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request, "Index.html",{})


def login(request,*args,**kwargs):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            next= request.GET.get("next")
            if next:
             return redirect(next)   
            return redirect("/about/")
        else:
            messages.info(request,"Invalid credentials")    

    return render(request,"Login.html",{})


@login_required(login_url="/login/")
def logout(request,*args,**kwargs):
    logout(request)
    return redirect("/login/")

def signup(request):

    if request.method== "POST":
        fname=request.POST['fname']
        uname=request.POST['username']
        gmail=request.POST['email']
        progie = request.POST['inlineRadioOptions']
        uni = request.POST['institution']
        whatsapp = request.POST['contact']
        field = request.POST['interest']
        sex = request.POST['gender']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        
        print(request.POST)
        if pass1== pass2:
            try:
                user = User.objects.create(
                    name= fname,
                    username = uname,
                    email = gmail,
                    program = progie,
                    institution = uni,
                    contact = whatsapp,
                    field_of_interest = field,
                    gender = sex,
                    password = pass1,
                )
                if request.FILES:
                    pp = request.FILES['pp']
                    UserProfile.objects.create (
                        owner = User.objects.get(id = user.id),
                        pp = pp
                    )
                    print("user account created successfully!!")
                messages.info(request,"user account created successfully!!")
                
            except Exception as e:
                print("user with the same Username Exits")
                messages.info(request,"user with the same Username Exits!!")
                print(e)
        else:
            print("passwords do not match") 
            messages.info(request,"passwords do not match")

    return render(request,"SignUp.html",{})

