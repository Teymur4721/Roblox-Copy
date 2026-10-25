from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='roblox_index'),
]