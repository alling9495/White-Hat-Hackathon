from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def home(request):
    page = HttpResponse('== OUR COOL WEB PAGE ==<br><br>\
    See more at <a href="https://www.duckduckgo.com">Google.com</a>')
    return page
