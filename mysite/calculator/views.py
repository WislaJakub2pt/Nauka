import numbers
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def hello(request , number):
    return HttpResponse(f"Hello, World! {number}")

@csrf_exempt
def calc(request):
    pass