from django.urls import path, re_path

from apps.pet.views import index,pet_view, pet_list, pet_edit, pet_delete
urlpatterns = [
    path('', index, name ='pets-index'),
    path('new', pet_view, name ='pets-new'),
    path('list', pet_list, name ='pets-list'),
    re_path('edit/(?P<id_pet>\d+)', pet_edit, name ='pets-edit'),
    re_path('delete/(?P<id_pet>\d+)', pet_delete, name ='pets-delete'),
]
