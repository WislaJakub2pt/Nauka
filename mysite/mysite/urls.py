from django.contrib import admin
from django.urls import include, path

from calculator.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('calculator.urls'))
]
