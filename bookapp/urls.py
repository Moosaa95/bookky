from bookapp.views import  layout
from django import views
from django.urls import path



urlpatterns = [
    path('', layout, name='layout')
]