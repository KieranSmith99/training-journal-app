from django.test import TestCase
from .models import Resource, Language, Framework, Database, Technology
from django.contrib.auth.models import User

# Create your tests here.


class ResourceTest(TestCase):

    def setUp(self):
        user = User.objects.create(username="Test User")
        Resource.objects.create(name="Google", link="https://google.com", created_by=user)

    def testCreate(self):
        resource = Resource.objects.get(name="Google")
        self.assertEqual(resource.name, "Google")

    def testNotExist(self):
        resource = Resource.objects.filter(name="Incorrect")
        self.assertEqual(len(resource), 0)

class LanguageTest(TestCase):

    def setUp(self):
        Language.objects.create(name="Python")

    def testCreate(self):
        language = Language.objects.get(name="Python")
        self.assertEqual(language.name, "Python")


class FrameworkTest(TestCase):

    def setUp(self):
        Framework.objects.create(name="Flask")

    def testCreate(self):
        framework = Framework.objects.get(name="Flask")
        self.assertEqual(framework.name, "Flask")


class DatabaseTest(TestCase):

    def setUp(self):
        Database.objects.create(name="PostgreSQL")

    def testCreate(self):
        database = Database.objects.get(name="PostgreSQL")
        self.assertEqual(database.name, "PostgreSQL")


class TechnologyTest(TestCase):

    def setUp(self):
        Technology.objects.create(name="AWS")

    def testCreate(self):
        technology = Technology.objects.get(name="AWS")
        self.assertEqual(technology.name, "AWS")
