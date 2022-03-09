from django.urls import path

from .views import (ResourceView, ResourceCreateView, ResourceDeleteView, ResourceUpdateView,
                    LanguageView, LanguageCreateView, LanguageDeleteView, LanguageUpdateView,
                    FrameworkCreateView, FrameworkView, FrameworkDeleteView, FrameworkUpdateView)
from . import views

urlpatterns = [
    path('', ResourceView.as_view(), name='home'),
    path('resource/new/', ResourceCreateView.as_view(), name="new-resource"),
    path('resource/<int:pk>/delete', ResourceDeleteView.as_view(), name="resource-delete"),
    path('resource/<int:pk>/update', ResourceUpdateView.as_view(), name="resource-update"),
    path('languages', LanguageView.as_view(), name="languages"),
    path('language/new/', LanguageCreateView.as_view(), name="new-language"),
    path('language/<int:pk>/delete', LanguageDeleteView.as_view(), name="language-delete"),
    path('language/<int:pk>/update', LanguageUpdateView.as_view(), name="language-update"),
    path('frameworks', FrameworkView.as_view(), name="frameworks"),
    path('framework/new/', FrameworkCreateView.as_view(), name="new-framework"),
    path('framework/<int:pk>/delete', FrameworkDeleteView.as_view(), name="framework-delete"),
    path('framework/<int:pk>/update', FrameworkUpdateView.as_view(), name="framework-update"),
]
