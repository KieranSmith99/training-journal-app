from django.urls import path

from .views import (ResourceView)
from . import views

urlpatterns = [
    path('', ResourceView.as_view(), name='home')
]
