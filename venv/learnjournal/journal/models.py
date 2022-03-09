from django.db import models
from django.urls import reverse

# Create your models here.

language_choices = (
    ('Java', 'Java'),
    ('Python', 'Python'),
    ('Typescript', 'Typescript'),
    ('Javascript', 'Javascript'),
    ('Go', 'Go')
)

framework_choices = (
    ('Flask', 'Flask'),
    ('Django', 'Django'),
    ('Angular', 'Angular'),
    ('React', 'React'),
    ('Vue', 'Vue'),
    ('Spring Boot', 'Spring Boot')
)

database_choices = (
    ('MySQL', 'MySQL'),
    ('PostgreSQL', 'PostgreSQL'),
    ('MongoDB', 'MongoDB'),
    ('SQLite', 'SQLite')
)

technology_choices = (
    ('AWS', 'AWS'),
    ('Git', 'Git'),
    ('Azure', 'Azure')
)


class Resource(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=100, blank=True)
    language = models.CharField(max_length=20, choices=language_choices)
    framework = models.CharField(max_length=20, choices=framework_choices)
    database = models.CharField(max_length=20, choices=database_choices)
    technology = models.CharField(max_length=20, choices=technology_choices)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resource-detail', kwargs={'pk': self.pk})
