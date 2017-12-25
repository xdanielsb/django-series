from django.urls import path

from apps.pet.views import index,pet_view
urlpatterns = [
    path('', index, name ='index'),
    path('new', pet_view, name ='new_register'),
]
