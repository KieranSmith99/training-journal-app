from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, CreateView, DeleteView, UpdateView, TemplateView)
from .models import Resource, Language, Framework, Database, Technology
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.


class ResourceView(ListView):
    model = Resource
    template_name = 'journal/home.html'
    context_object_name = 'resources'


class UserResourceView(ListView):
    model = Resource
    template_name = 'journal/user_resources.html'
    context_object_name = 'resources'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Resource.objects.filter(created_by=user)


class SearchView(TemplateView):
    model = Resource
    template_name = 'journal/home.html'
    context_object_name = 'resources'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('searchInput')
        self.resources = Resource.objects.filter(name__icontains=query)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(resources=self.resources, **kwargs)


class ResourceCreateView(LoginRequiredMixin, CreateView):
    model = Resource
    fields = ['name', 'link', 'attachment', 'language', 'framework', 'database', 'technology']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ResourceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resource
    success_url = '/'

    def test_func(self):
        resource = self.get_object()
        if self.request.user == resource.created_by:
            return True
        return False


class ResourceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resource
    fields = ['name', 'link', 'attachment', 'language', 'framework', 'database', 'technology']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        resource = self.get_object()
        if self.request.user == resource.created_by:
            return True
        return False


class LanguageView(ListView):
    model = Language
    template_name = 'journal/language_list.html'
    context_object_name = 'languages'


class LanguageCreateView(LoginRequiredMixin, CreateView):
    model = Language
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class LanguageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Language
    success_url = '/languages'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class LanguageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Language
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class FrameworkView(ListView):
    model = Framework
    template_name = 'journal/framework_list.html'
    context_object_name = 'frameworks'


class FrameworkCreateView(LoginRequiredMixin, CreateView):
    model = Framework
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class FrameworkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Framework
    success_url = '/frameworks'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class FrameworkUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Framework
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class DatabaseView(ListView):
    model = Database
    template_name = 'journal/database_list.html'
    context_object_name = 'databases'


class DatabaseCreateView(LoginRequiredMixin, CreateView):
    model = Database
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class DatabaseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Database
    success_url = '/databases'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class DatabaseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Database
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class TechnologyView(ListView):
    model = Technology
    template_name = 'journal/technology_list.html'
    context_object_name = 'technologies'


class TechnologyCreateView(LoginRequiredMixin, CreateView):
    model = Technology
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class TechnologyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Technology
    success_url = '/technologies'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class TechnologyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Technology
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
