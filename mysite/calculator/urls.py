from django.contrib import admin
from django.urls import include, path

from calculator.views import hello , calc

urlpatterns = [
    path("hello/<int:number>",hello),
    path("calc", calc)
]