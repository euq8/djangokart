from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def home_simple_text(request):
    return HttpResponse('Homepage')

