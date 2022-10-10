from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('Home',views.home,name="Home"),
    path('reserve',views.reserve,name="Reservations"),
    path('Excursion',views.Excursion,name="Excursion")
]