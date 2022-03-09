from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import (ListView, CreateView, DeleteView, DetailView, UpdateView)
from .models import Resource

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
    fields = ['name', 'link', 'language', 'framework', 'database', 'technology']

    def form_valid(self, form):
        return super().form_valid(form)


class ResourceDeleteView(DeleteView):
    model = Resource
    success_url = '/'


class ResourceDetailView(DetailView):
    model = Resource


class ResourceUpdateView(UpdateView):
    model = Resource
    fields = ['name', 'link', 'language', 'framework', 'database', 'technology']

    def form_valid(self, form):
        return super().form_valid(form)
