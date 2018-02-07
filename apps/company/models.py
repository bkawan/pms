from django.conf import settings
from django.db import models
# Create your models here.
from django.db.models import TextField
from django.utils.safestring import mark_safe

from apps.core.models import AbstractImageEntry, AbstractCreatedAtUpdatedAt, AbstractCategory
from apps.core.utils import image_upload_to, unique_slugify


class CompanyDetail(models.Model):
    """Company Profile."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = TextField()
    logo = models.ImageField(upload_to=image_upload_to)
    featured_image = models.ImageField(upload_to=image_upload_to, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    phone3 = models.CharField(max_length=15, blank=True, null=True)
    phone4 = models.CharField(max_length=15, blank=True, null=True)
    facebook = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    google_plus = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        """Return name of the Company."""
        return self.name

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super().save(*args, **kwargs)


class TeamMember(models.Model):
    """Store Team Member profile."""

    company = models.ForeignKey(CompanyDetail, related_name='team_members', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_to)
    joined_date = models.DateField(max_length=10)
    facebook = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    google_plus = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        """Store Team Members."""
        return self.name


class Service(AbstractImageEntry, AbstractCreatedAtUpdatedAt):
    """Service of the company."""

    company = models.ForeignKey(CompanyDetail, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon = models.ImageField(upload_to=image_upload_to, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        """Return service name."""
        return self.name

    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super().save(*args, **kwargs)


class Testimonial(AbstractCreatedAtUpdatedAt):
    """Testimonial of the company."""

    company = models.ForeignKey(CompanyDetail, related_name='testimonials', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_to)
    organization = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name

        # def save(self, *args, **kwargs):
        #     self.company = CompanyDetail.objects.first()
        #     super().save(*args, **kwargs)


class HomePageTopImageSlider(models.Model):
    """Top Banner Image Slider."""

    company = models.ForeignKey(CompanyDetail, related_name='sliders', on_delete=models.CASCADE)
    caption = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to=image_upload_to)
    description = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        """Return image object."""
        return str(self.image.name)

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="84" height="84" />'.format(self.image.url))

    image_tag.short_description = 'Slider'


class Client(models.Model):
    """Stores Client Basic Profile."""

    company = models.ForeignKey(CompanyDetail, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to=image_upload_to)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        """Return client name."""
        return self.name

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="84" height="84" />'.format(self.logo.url))

    image_tag.short_description = 'Logo'
