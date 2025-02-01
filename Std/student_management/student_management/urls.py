from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Student Management System</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),  # Include the URLs from the 'students' app
    path('', home, name='home'),  # Add a root URL
    
]
