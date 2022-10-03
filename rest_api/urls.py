from django.urls import path, include
from .views import home, krosovkaMakeAPI, singleAPI, MashinaMakeAPI, bittaAPI

app_name = "api"

urlpatterns = [
    path('', home, name="home"),
    path('krosovka-api/', krosovkaMakeAPI),
    path('krosovka-api/<int:pk>/', singleAPI),
    path('mashina-api/', MashinaMakeAPI),
    path('mashina-api/<int:pk>/', bittaAPI),
]

.ppya