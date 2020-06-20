from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "mywebsite/home.html",)

def aboutMe(request):
    return render(request, "mywebsite/aboutMe.html")

def myWorks(request):
    return render(request, "mywebsite/myWorks.html")

def myResume(request):
    return render(request, "mywebsite/myResume.html")

def contactMe(request):
    return render(request, "mywebsite/contactMe.html")