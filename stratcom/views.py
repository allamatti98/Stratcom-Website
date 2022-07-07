from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return render(request, "Login1.html", {})

def index2(request):
    return render(request, "Login2.html", {})

def index3(request):
    return render(request,"Login3.html",{})

def index4(request):
    return render(request, "Login4.html", {})


def index5(request):
    return render(request, "Login5.html", {})

def signup1(request):
    return render(request,"Signup.html",{})

def signup2(request):
    return render(request,"Signup1.html",{})

def signup3(request):
    return render(request, "Signup2.html", {})

def signup4(request):
    return render(request,"Signup3.html",{})

def gallery1(request):
    return render(request, "gallery.html", {})

def gallery2(request):
    return render(request,"Gallery1.html",{})

def gallery3(request):
    return render(request, "Gallery2.html", {})

def gallery4(request):
    return render(request,"Gallery3.html",{})

def aboutus(request):
    return render(request, "AboutUs.html", {})

def homepage(request):
    return render(request,"homepage.html",{})