from django.urls import path, include
from .views import home, krosovkaMakeAPI

app_name = "api"

urlpatterns = [
    path('', home, name="home"),
    path('krosovka-api/', krosovkaMakeAPI),
]