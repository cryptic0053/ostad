from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.
def home(request):
    print(request.POST)  # Debugging to see received data

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        student = models.Student(name=name, email=email, phone=phone, password=password)
        student.save()
        
        return HttpResponse("Student Object Created Successfully")

    return render(request, 'student/index.html')
