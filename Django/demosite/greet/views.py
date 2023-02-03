# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "greet/index.html")

def greet(request, name):
    return render(request, "greet/greet.html",{
        "name" : name.capitalize()
    })