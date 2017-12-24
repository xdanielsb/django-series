from django.urls import path

from apps.pet.views import index
urlpatterns = [
    path('', index),
    path('index/', index),
]
