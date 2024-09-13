# petsapp/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pet

class PetListView(ListView):
    model = Pet
    template_name = 'pet_list.html'

class PetCreateView(CreateView):
    model = Pet
    template_name = 'pet_form.html'
    fields = ['first_name', 'last_name', 'email', 'phone_number']
    success_url = reverse_lazy('pet_list')  # Redirect to pet list after creation

class PetUpdateView(UpdateView):
    model = Pet
    template_name = 'pet_form.html'
    fields = ['first_name', 'last_name', 'email', 'phone_number']
    success_url = reverse_lazy('pet_list')  # Redirect to pet list after update

class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pet_confirm_delete.html'
    success_url = reverse_lazy('pet_list')  # Redirect to pet list after deletion
