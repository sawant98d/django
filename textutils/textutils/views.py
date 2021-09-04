# I have created this views.py file :- sawant98d
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello welcome page</h1>")

def about(request):
    return HttpResponse("<h4>About page</h4>")

def get_links(request):
    return HttpResponse('''
    <h1>
        <a href="https://www.facebook.com/">facebook</a><br/>
        <a href="https://www.google.com/">Google</a><br/>
        <a href="https://www.amazon.com/">Amazon</a><br/>
        <a href="https://www.adobe.com/">Adobe</a><br/>
    </h1>
    ''')
