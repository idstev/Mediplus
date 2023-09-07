from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('medicine/',views.medicine,name="medicine"),
    path('news/',views.news,name="news"),
]