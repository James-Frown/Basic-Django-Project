from django.urls import path
from . import views

app_name='roulette'

urlpatterns = [
    path('home', views.RouletteHome.as_view(), name="roulette_home")
]
