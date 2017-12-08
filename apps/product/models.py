from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from apps.company.models import CompanyDetail
from apps.core.models import AbstractCreatedAtUpdatedAt, AbstractImageEntry, AbstractCategory
from apps.core.utils import image_upload_to, unique_slugify


class ProductCategory(AbstractCategory) :
    """Category for products."""

    class Meta :
        verbose_name = _('product category')
        verbose_name_plural = _('product categories')


class Product(AbstractCreatedAtUpdatedAt) :
    """Products."""

    company = models.ForeignKey(CompanyDetail, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    specification = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    categories = models.ManyToManyField(ProductCategory, blank=True)
    slug = models.SlugField(unique=True, max_length=255)
    featured_image = models.ImageField(upload_to=image_upload_to)

    def __str__(self) :
        """Return product."""
        return str(self.name)

    def save(self, *args, **kwargs) :
        unique_slugify(self, self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self) :
        return reverse('product:detail', args=[str(self.slug)])


class ProductImage(AbstractCreatedAtUpdatedAt, AbstractImageEntry) :
    """Product's Images."""
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self) :
        """Return product name of the image."""
        return '{} - {}'.format(self.product, self.image_title)
