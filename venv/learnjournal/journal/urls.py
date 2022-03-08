from django.urls import path

from .views import (ResourceView, ResourceCreateView)
from . import views

urlpatterns = [
    path('', ResourceView.as_view(), name='home'),
    path('resource/new/', ResourceCreateView.as_view(), name="new-resource")
]
