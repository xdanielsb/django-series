from django.urls import path

from apps.adoption.views import index
urlpatterns = [
    path('', index),
]
