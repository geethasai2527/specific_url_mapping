from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('this is my first view in app2')
def second(request):
    return HttpResponse('this is my second view in app2')
