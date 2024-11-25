from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def FrontEnd(request):
    return HttpResponse('<h1>It is used along with html and css</h1>')