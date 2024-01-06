from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import csv
from django.core.cache import cache


# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional custom fields
    middle_name = models.CharField(max_length=30, blank=True, verbose_name=_('Middle Name'))
    alias = models.CharField(max_length=30, blank=True, verbose_name=_('Alias'))
    title = models.CharField(max_length=100, blank=True, verbose_name=_('Title'))
    mobile = models.CharField(max_length=15, blank=True, verbose_name=_('Mobile'))
    npi_number = models.CharField(max_length=20, blank=True, verbose_name=_('NPI Number'))
    dea_number = models.CharField(max_length=20, blank=True, verbose_name=_('DEA Number'))
    nadean_number = models.CharField(max_length=20, blank=True, verbose_name=_('NADEAN Number'))
    #state_license = models.CharField(max_length=20, blank=True, verbose_name=_('State License'), choices= get_state_choices())
    primary_license_number = models.CharField(max_length=30, blank=True, verbose_name=_('Primary License Number'))
    secondary_license_number = models.CharField(max_length=30, blank=True, verbose_name=_('Secondary License Number'))
    email = models.EmailField(unique=True, verbose_name=_('Email Address'))
    
    # Notification preferences (you can customize this based on your requirements)
    receive_text_notifications = models.BooleanField(default=False, verbose_name=_('Receive Text Notifications'))
    receive_call_notifications = models.BooleanField(default=False, verbose_name=_('Receive Call Notifications'))


    state_license = models.CharField(max_length=20, blank=True, verbose_name=_('State License'))

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)
        self._meta.get_field('state_license').choices = self.get_state_choices()

    @staticmethod
    def get_state_choices():
        state_choices = cache.get('state_choices')
        if state_choices is None:
            
            with open('core\\configuration\\US_States.csv', 'r') as f:
                reader = csv.reader(f)
                state_choices = [(row[0], row[1]) for row in reader]
            cache.set('state_choices', state_choices, 60 * 60 * 24)  # Cache results for 24 hours
        return state_choices

    # Add any other fields or methods as needed

    def __str__(self):
        return self.user.username  # You can change this to display the user's name or other identifier

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

