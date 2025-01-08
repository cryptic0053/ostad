from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def profile(request):
#     return HttpResponse("This is student profile page")

def profile(request):
    user_data = {
        'name': 'John Doe',
        'age': 10,
    }
    marks = [
        {
            'id': '1',
            'subject': 'Maths',
            'marks': 85
        },
        {
            'id': '2',	
            'subject': 'Science',
            'marks': 90
        },
        {
            'id': '3',
            'subject': 'English',
            'marks': 80
        },
        {
            'id': '4',
            'subject': 'History',
            'marks': 75
        }
    ]
    return render(request, 'student/index.html', {'marks': marks , 'age' : 20 ,'Name': 'John Doe'})

def home(request):
    return HttpResponse("This is student home page")