from django.urls import path
from . import views

urlpatterns = [
    path('',views.healt,name="healt"),
]