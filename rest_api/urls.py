from django.urls import path, include
from .views import home

app_name = "api"

urlpatterns = [
    path('', home, name="home"),
]