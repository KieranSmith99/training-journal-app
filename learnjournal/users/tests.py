from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class UserTest(TestCase):

    def setUp(self):
        User.objects.create(username="TestUser")

    def testCreate(self):
        user = User.objects.get(username="TestUser")
        self.assertEqual(user.username, "TestUser")
