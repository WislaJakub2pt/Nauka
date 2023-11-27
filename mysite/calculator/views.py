import json
import numbers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from calculator.models import User


def hello(request , number):
    return HttpResponse(f"Hello, World! {number}")

@csrf_exempt
def calc(request):
    data = json.loads(request.body)
    if data["operation"] == "+":
        result = data["a"] + data["b"]
        return HttpResponse(f"{result}")

def get_users(request):
    users = User.object.all()
    users_data = []
    for user in users:
        users_data.append(user.username)
    
    return JsonResponse({"users":users_data})