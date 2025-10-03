from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
        return render(request, "home.html")

def greet(request, name):
    context ={
        "name": name.capitalize()
        }
    return render(request, 'greet.html', context)
    