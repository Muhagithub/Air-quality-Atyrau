from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("weather-atyrau", views.weather),
    path("index-russian", views.russian),
    path("index-english", views.english),
    path("weather-russian", views.weather_russian),
    path("weather-english", views.weather_english),
]

