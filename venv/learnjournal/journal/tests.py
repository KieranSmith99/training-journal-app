from django.test import TestCase, RequestFactory
from .models import Resource
from .views import ResourceView

# Create your tests here.


class ResourceTest(TestCase):

    def setUp(self):
        Resource.objects.create(name="Google", link="https://google.com")

    def testCreate(self):
        resource = Resource.objects.get(name="Google")
        self.assertEqual(resource.name, "Google")
