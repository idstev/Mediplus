from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def medicine(request):
    return render(request, "core/medicine.html")

def news(request):
    return render(request, "core/news.html")


