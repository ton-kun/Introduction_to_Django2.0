from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello woeld")

def foo(request):
    return HttpResponse("Foo")

def woo(request):
    return HttpResponse("woo")

def hoge(request):
    if request.method == 'POSt':
        return HttpResponse("Hoge")
    elif request.method == 'GET':
        return HttpResponse("hoge")
    else:
        return HttpResponse("Foo")
