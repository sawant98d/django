# I have created this views.py file :- sawant98d
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello welcome page</h1>")

def about(request):
    return HttpResponse("<h4>About page</h4>")
