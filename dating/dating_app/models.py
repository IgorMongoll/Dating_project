from django.db import models
from PIL import Image
#from .dating_app.choices_for_models import *
from .choices_for_models import *




class UserProfile(models.Model):

    name = models.CharField(max_length=100, verbose_name='Name')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Gender')
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    bundesland = models.CharField(max_length=2, choices=BUNDESLAND_CHOICES, blank=True, null=True, verbose_name='Bundesland')
    language = models.CharField(max_length=100, blank=True, null=True, verbose_name='Language')
    height = models.PositiveIntegerField(blank=True, null=True, verbose_name='Height (in cm)')
    weight = models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight (in kg)')
    eye_color = models.CharField(max_length=10, choices=EYE_COLOR_CHOICES, blank=True, null=True, verbose_name='Eye Color')
    hair_color = models.CharField(max_length=10, choices=HAIR_COLOR_CHOICES, blank=True, null=True, verbose_name='Hair Color')
    education = models.CharField(max_length=11, choices=EDUCATION_CHOICES, blank=True, null=True, verbose_name='Education')
    occupation = models.CharField(max_length=10, choices=OCCUPATION_CHOICES, blank=True, null=True, verbose_name='Occupation')
    hobbies = models.TextField(blank=True, null=True, verbose_name='Hobbies')
    interests = models.TextField(blank=True, null=True, verbose_name='Interests')
    bio = models.TextField(blank=True, null=True, verbose_name='Bio')

    # New fields for dating purposes
    relationship_purpose = models.CharField(
        max_length=20,
        choices=RELATIONSHIP_PURPOSE_CHOICES,
        blank=True,
        null=True,
        verbose_name='Relationship Purpose'
    )

    looking_for = models.CharField(
        max_length=10,
        choices=LOOKING_FOR_CHOICES,
        blank=True,
        null=True,
        verbose_name='Looking For'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
