# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
 
 
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def home(request):
	return render(request, 'home.html')