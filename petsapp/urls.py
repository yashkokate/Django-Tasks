from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('service/', views.service_page, name='service_page'),
    path('contact/', views.contact_us, name='contact_us'),
]
