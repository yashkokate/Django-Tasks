# petsapp/views.py

from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def service_page(request):
    return render(request, 'service.html')

def contact_us(request):
    return render(request, 'contact_us.html')
