from django.urls import path

from .views import (ResourceView, ResourceCreateView, ResourceDeleteView, ResourceUpdateView,
                    LanguageView, LanguageCreateView, LanguageDeleteView, LanguageUpdateView,
                    FrameworkCreateView, FrameworkView, FrameworkDeleteView, FrameworkUpdateView,
                    DatabaseView, DatabaseCreateView, DatabaseUpdateView, DatabaseDeleteView,
                    TechnologyView, TechnologyCreateView, TechnologyDeleteView, TechnologyUpdateView,
                    SearchView)

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
    path('databases', DatabaseView.as_view(), name="databases"),
    path('database/new/', DatabaseCreateView.as_view(), name="new-database"),
    path('database/<int:pk>/delete', DatabaseDeleteView.as_view(), name="database-delete"),
    path('database/<int:pk>/update', DatabaseUpdateView.as_view(), name="database-update"),
    path('technologies', TechnologyView.as_view(), name="technologies"),
    path('technology/new/', TechnologyCreateView.as_view(), name="new-technology"),
    path('technology/<int:pk>/delete', TechnologyDeleteView.as_view(), name="technology-delete"),
    path('technology/<int:pk>/update', TechnologyUpdateView.as_view(), name="technology-update"),
    path('search', SearchView.as_view(), name="search")
]
