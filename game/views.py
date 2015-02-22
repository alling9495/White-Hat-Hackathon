from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return profile(request)

def home(request):
    page = HttpResponse('== OUR COOL WEB PAGE ==<br><br>\
    See more at <a href="https://www.duckduckgo.com">Google.com</a>')
    return page

def profile(request):
    page = HttpResponse('<img src="https://www.zazzle.com/rlv/youre_winner_postcards-r9b5dc3c531534145832f8d37fb57e808_vgbaq_8byvr_512.jpg">')
    return page
