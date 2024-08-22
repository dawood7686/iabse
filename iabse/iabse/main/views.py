from django.shortcuts import render

# Create your views here.

def Homepage(request):
    return render(request, "homepage.html")

def Onlinecourse(request):
    return render(request, "")

def Login(request):
    return render(request, "login.html")

def Forgetpassword(request):
    return render(request, "forgetpassword.html")

def Coursesubcategories(request):
    return render(request, "coursesubcategories.html")