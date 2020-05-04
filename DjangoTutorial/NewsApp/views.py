from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def Home(request):
    return HttpResponse("This is home page")

def News(request):
    return HttpResponse("<h1> this is news </h1>")

def Contact(request):
    return HttpResponse("<h1> this is contact </h1>")
