import os

from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
from django.utils.text import slugify

from apps.core.utils import image_upload_to

TITLE_CHOICES = (
    ("Mr", "Mr"),
    ("Mrs", "Mrs"),
    ("Miss", "Miss"),
    ("Dr", "Dr"),
    ("Er", "Er"),
    ("Sir", "Sir"),
)
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others"),
)


@python_2_unicode_compatible
class User(AbstractUser):
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to=image_upload_to, null=True, blank=True)

    def __str__(self):
        return '{} {} - {}'.format(self.first_name, self.last_name, self.username)
