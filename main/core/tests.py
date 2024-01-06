# Create your tests here.
from django.test import TestCase
from django import setup
import os
from .models import Profile
from django.contrib.auth.models import User


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
setup()


class ProfileModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_add_profile(self):
        # Create a new Profile instance
        profile = Profile.objects.create(
            user=self.user,
            middle_name='Test Middle Name',
            alias='Test Alias',
            title='Test Title',
            mobile='Test Mobile',
            npi_number='Test NPI Number',
            dea_number='Test DEA Number',
            nadean_number='Test NADEAN Number',
            primary_license_number='Test Primary License Number',
            secondary_license_number='Test Secondary License Number',
            email='test@example.com',
            receive_text_notifications=True,
            receive_call_notifications=True,
            state_license='Test State License',
        )
        
        # Retrieve the profile from the database and check if it was saved correctly
        saved_profile = Profile.objects.get(user=self.user)
        self.assertEqual(saved_profile.middle_name, 'Test Middle Name')
        # Add similar assertions for other fields

    def test_change_profile(self):
        # Create an initial Profile instance
        profile = Profile.objects.create(
            user=self.user,
            middle_name='Initial Middle Name',
            # Add other initial field values
        )
        
        # Change some fields in the Profile instance
        profile.middle_name = 'Changed Middle Name'
        # Change other fields as needed
        profile.save()

        # Retrieve the profile from the database and check if changes were saved correctly
        updated_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_profile.middle_name, 'Changed Middle Name')
        # Add similar assertions for other fields

    def test_delete_profile(self):
        # Create a Profile instance
        profile = Profile.objects.create(
            user=self.user,
            middle_name='Test Middle Name',
            # Add other field values
        )

        # Delete the Profile instance
        profile.delete()

        # Verify that the profile has been deleted from the database
        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(user=self.user)
