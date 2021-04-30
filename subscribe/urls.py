from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_subscribe, name='subscribe'),
]