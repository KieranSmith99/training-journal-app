from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import (ListView)
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
