from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def profile(request):
#     return HttpResponse("This is student profile page")

def profile(request):
    return render(request, 'student/index.html')

def home(request):
    return HttpResponse("This is student home page")