# I have created this views.py file :- sawant98d
from django.http import HttpResponse
from django.shortcuts import render

"""
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
"""
def index(request):
    #return HttpResponse("<a href='/'>Back</a><h1>Hello welcome page</h1>")
    params = {'name':'Dadasaheb', 'place':'India'}
    return render(request,'index.html',params)

def removepunc(request):
    return HttpResponse("<a href='/'>Back</a>removepunc")

def capitalizefirst(request):
    return HttpResponse("<a href='/'>Back</a>capitalizefirst")

def newlineremove(request):
    return HttpResponse("<a href='/'>Back</a>newlineremove")

def spaceremove(request):
    return HttpResponse('spaceremove')

def charcount(request):
    return HttpResponse('charcount')
