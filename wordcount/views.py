from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse('<h1>YO WHATSUP</h1>')

def count(request):
    return render(request, 'count.html')