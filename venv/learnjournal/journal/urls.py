from django.urls import path

from .views import (ResourceView)
from . import views

urlpatterns = [
    path('', views.home, name='home')
]
