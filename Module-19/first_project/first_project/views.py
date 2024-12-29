from django.http import HttpResponse

def home(request):
    print("hello")
    return HttpResponse("<h1>Hello</h1>")