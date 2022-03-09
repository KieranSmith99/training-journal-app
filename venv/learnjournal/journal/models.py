from django.db import models
from django.urls import reverse

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('languages')


class Framework(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('frameworks')


class Database(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('databases')


class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('technologies')


class Resource(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=100, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    framework = models.ForeignKey(Framework, on_delete=models.CASCADE, blank=True, null=True)
    database = models.ForeignKey(Database, on_delete=models.CASCADE, blank=True, null=True)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
