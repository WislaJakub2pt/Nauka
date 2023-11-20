from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")
def factoria(request):
    
    return HttpResponse("Tu bedzie silnia")