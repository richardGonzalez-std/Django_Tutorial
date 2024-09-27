from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'Hello/index.html')

def name(request):
    return HttpResponse("Hello Richard!")

def greet(request,name):
    return render(request, 'Hello/greet.html',{
        'name': name.capitalize()
    })