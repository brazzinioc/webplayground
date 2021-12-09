from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile



# Create your tests here.

# Unit tests for the Profile model
class ProfileTestCase(TestCase):
    def setUp(self):
      User.objects.create_user(username='testuser', email='my_email@gmail.com', password='ueueuur@*12345')

    def test_profile_exit(self):
      exist = Profile.objects.filter(user__username='testuser').exists()
      self.assertEqual(exist, True)

