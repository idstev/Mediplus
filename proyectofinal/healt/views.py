from django.shortcuts import render
from .models import Healt
# Create your views here.
def healt(request):
    healts= Healt.objects.all()
    return render(request, "healt/healt.html", {'listHealts':healts})
