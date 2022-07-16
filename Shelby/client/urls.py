from django.contrib import admin
from django.urls import path
from .views import client, create_client, see_client

urlpatterns = [
    path('clients/', client , name = 'clients'),
    path('create-client/', create_client , name = 'create-client'),
    path('see-client/',see_client , name = 'see-client'),
]