from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('current_time', views.current_time)
]