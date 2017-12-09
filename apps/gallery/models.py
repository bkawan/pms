from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from apps.company.models import CompanyDetail
from apps.core.models import AbstractCategory, AbstractImageEntry, AbstractCreatedAtUpdatedAt
from apps.core.utils import unique_slugify, image_upload_to


class AlbumCategory(AbstractCategory) :
    """Category for Galleries."""

    class Meta :
        verbose_name = _('Album category')
        verbose_name_plural = _('Album categories')


class Album(AbstractCreatedAtUpdatedAt) :
    """Name of Album."""
    company = models.ForeignKey(CompanyDetail, related_name='albums', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(AlbumCategory, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255)
    featured_image = models.ImageField(upload_to=image_upload_to)

    def __str__(self) :
        """Return Album object."""
        return self.name

    def save(self, *args, **kwargs) :
        unique_slugify(self, self.name)
        super().save(*args, **kwargs)


class AlbumImage(AbstractImageEntry, AbstractCreatedAtUpdatedAt) :
    """Image for the Album."""
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)

    def __str__(self) :
        """Return Image object."""
        return '{} - {}'.format(self.album, self.image_title)
