from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Easy(request):
    return HttpResponse("<h1>Very Easy Language</h1>")
