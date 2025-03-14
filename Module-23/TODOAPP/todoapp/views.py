from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.

def hello(request):
    return HttpResponse("Hello, World!")

@login_required
def hello_protected(request):
    return HttpResponse("Hello, World! This is a protected page.")

def index(request):
    return HttpResponse("Welcome")


