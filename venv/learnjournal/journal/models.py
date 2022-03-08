from django.db import models

# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=100)

    def __str__(self):
        return self.title
