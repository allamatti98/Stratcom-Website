import email
from multiprocessing import context
from urllib import response
from django.forms import PasswordInput
from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from setuptools import find_namespace_packages
import json
from . models import UserProfile,Gallery, User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
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
            auth_login(request, user)
            print("We almost there!!!")
            print("We almost there!!!")
            print("We almost there!!!")
            return redirect('index')
        else:
            messages.info(request,"Invalid credentials")    

    return render(request,"Login.html",{})


@login_required(login_url="/login/")
def logout(request,*args,**kwargs):
    logout(request)
    return redirect("/login/")

def signup(request,*args,**kwargs):

    if request.method== "POST":
        fname=request.POST['fname']
        uname=request.POST['username']
        email=request.POST['email']
        progie = request.POST['inlineRadioOptions']
        institution = request.POST['institution']
        whatsapp = request.POST['number']
        field = request.POST['interest']
        sex = request.POST['gender']
        pp = request.POST['pp']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        print("wazza")
        
        print(request.POST)
        if pass1== pass2:
            print(pass1)
            try:
                user = User.objects.create_user(uname, email, pass1 )
                user.name = fname
                user.program = progie
                user.institution = institution
                user.number = whatsapp
                user.field_of_interest = field
                user.gender = sex
                user.placement_letter = pp
                user.save()
                
                if request.FILES:
                    pp = request.FILES['pp']
                    UserProfile.objects.create (
                        owner = User.objects.get(id = user.id),
                        pp = pp
                    )
                    return redirect("/login/")
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


def error404(request, exception, template_name = '404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response