from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
from django.conf import settings


class Company(models.Model):
    NAME_MAX_LEN = 100
    ORIGIN_MAX_LEN = 100
    SECTOR_MAX_LEN = 100
    TYPE_MAX_LEN = 100

    name = models.CharField(max_length=NAME_MAX_LEN, unique=True)
    slug = models.SlugField(unique=True)
    origin = models.CharField(
        max_length=ORIGIN_MAX_LEN,
        choices=settings.COMPANY_ORIGIN_CHOICES,
        blank=True,
    )
    sector = models.CharField(
        max_length=SECTOR_MAX_LEN,
        choices=settings.COMPANY_SECTOR_CHOICES,
        blank=True,
    )
    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        choices=settings.COMPANY_TYPE_CHOICES,
        blank=True,
    )
    site = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name

    def site_link(self):
        return format_html('<a href="{0}">{0}</a>', self.site)
