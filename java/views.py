from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Hard(request):
    return HttpResponse('<h1>It is a very hard to learn java</h1>')