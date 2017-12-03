from django.db import models
# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager
from mptt.models import MPTTModel

from apps.core.utils import image_upload_to


@python_2_unicode_compatible
class AbstractCategory(MPTTModel):
    """
    Simple model for categorizing entries.
    """

    title = models.CharField(
        _('title'), max_length=255, unique=True)

    slug = models.SlugField(
        _('slug'), unique=True, max_length=255,
        help_text=_("Used to build the category's URL."))

    description = models.TextField(
        _('description'), blank=True)

    parent = TreeForeignKey(
        'self',
        related_name='children',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('parent category'))

    objects = TreeManager()

    @property
    def is_parent(self):
        if not self.parent_id:
            return True

    @property
    def tree_path(self):
        """
        Returns category's tree path
        by concatening the slug of his ancestors.
        """
        if self.parent_id:
            return '/'.join(
                [ancestor.slug for ancestor in self.get_ancestors()] +
                [self.slug])
        return self.slug

    def __str__(self):
        return self.title

    class Meta:
        """
        Category's meta informations.
        """
        abstract = True
        ordering = ['title']
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    class MPTTMeta:
        """
        Category MPTT's meta informations.
        """
        order_insertion_by = ['title']


class AbstractCreatedAtUpdatedAt(models.Model):
    created_at = models.DateTimeField(_('Created At.'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At.'), auto_now=True)

    class Meta:
        abstract = True


class AbstractImageEntry(models.Model):
    image_title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(
        _('image'), blank=True,
        upload_to=image_upload_to,
        help_text=_('Image for the Content'))

    image_caption = models.CharField(
        _('caption'), blank=True, null=True, max_length=255,
        help_text=_("Image's caption."))

    image_source = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True
