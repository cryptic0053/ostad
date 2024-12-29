from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profile(request):
    return HttpResponse("This is teacher profile page")

def home(request):
    return HttpResponse("This is teacher home page")