from django.urls import path
from .views import PetListView, PetCreateView, PetUpdateView, PetDeleteView

urlpatterns = [
    path('', PetListView.as_view(), name='pet_list'),
    path('pet/add/', PetCreateView.as_view(), name='pet_add'),
    path('pet/<int:pk>/edit/', PetUpdateView.as_view(), name='pet_edit'),
    path('pet/<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete'),
]
