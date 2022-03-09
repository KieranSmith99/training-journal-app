from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import (ListView, CreateView, DeleteView, DetailView, UpdateView)
from .models import Resource, Language, Framework, Database, Technology

# Create your views here.


def home(request):
    context = {
        'resources': Resource.objects.all()
    }

    return render(request, 'journal/home.html', context)


class ResourceView(ListView):
    model = Resource
    template_name = 'journal/home.html'
    context_object_name = 'resources'


class ResourceCreateView(CreateView):
    model = Resource
    fields = ['name', 'link', 'attachment', 'language', 'framework', 'database', 'technology']

    def form_valid(self, form):
        return super().form_valid(form)


class ResourceDeleteView(DeleteView):
    model = Resource
    success_url = '/'

    def test_func(self):
        resource = self.get_object()


class ResourceUpdateView(UpdateView):
    model = Resource
    fields = ['name', 'link', 'attachment', 'language', 'framework', 'database', 'technology']

    def form_valid(self, form):
        return super().form_valid(form)


class LanguageView(ListView):
    model = Language
    template_name = 'journal/language_list.html'
    context_object_name = 'languages'


class LanguageCreateView(CreateView):
    model = Language
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class LanguageDeleteView(DeleteView):
    model = Language
    success_url = '/languages'

    def test_func(self):
        language = self.get_object()


class LanguageUpdateView(UpdateView):
    model = Language
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class FrameworkView(ListView):
    model = Framework
    template_name = 'journal/framework_list.html'
    context_object_name = 'frameworks'


class FrameworkCreateView(CreateView):
    model = Framework
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class FrameworkDeleteView(DeleteView):
    model = Framework
    success_url = '/frameworks'

    def test_func(self):
        framework = self.get_object()


class FrameworkUpdateView(UpdateView):
    model = Framework
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class DatabaseView(ListView):
    model = Database
    template_name = 'journal/database_list.html'
    context_object_name = 'databases'


class DatabaseCreateView(CreateView):
    model = Database
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class DatabaseDeleteView(DeleteView):
    model = Database
    success_url = '/databases'

    def test_func(self):
        database = self.get_object()


class DatabaseUpdateView(UpdateView):
    model = Database
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class TechnologyView(ListView):
    model = Technology
    template_name = 'journal/technology_list.html'
    context_object_name = 'technologies'


class TechnologyCreateView(CreateView):
    model = Technology
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)


class TechnologyDeleteView(DeleteView):
    model = Technology
    success_url = '/technologies'

    def test_func(self):
        technology = self.get_object()


class TechnologyUpdateView(UpdateView):
    model = Technology
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)
