from django.urls import path

from .views import (ResourceView, ResourceCreateView, ResourceDetailView, ResourceDeleteView)
from . import views

urlpatterns = [
    path('', ResourceView.as_view(), name='home'),
    path('resource/new/', ResourceCreateView.as_view(), name="new-resource"),
    path('resource/<int:pk>/', ResourceDetailView.as_view(), name="resource-detail")
]
