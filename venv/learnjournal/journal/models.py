from django.db import models
from django.urls import reverse

# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resource-detail', kwargs={'pk': self.pk})
