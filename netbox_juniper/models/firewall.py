from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search


class FirewallFilter(NetBoxModel):
    name = models.CharField(max_length=64, blank=False)
    family = models.CharField(max_length=20, 
        choices=[
            ('inet', 'IPv4'),
            ('inet6', 'IPv6'),
            ('ethernet-switching', 'Layer 2'),
        ]
    )
    comments = models.TextField(blank=True)
    device = models.ForeignKey('dcim.Device', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Firewall Filter")
        verbose_name_plural = _("Firewall Filters")
        ordering = ['device','name']
        constraints = [
            models.UniqueConstraint(
                fields=['device', 'name'],
                name='unique_firewall_filter'
            )
        ]
        indexes = [
            models.Index(fields=['name'], name='idx_firewall_filter_name'),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_juniper:firewallfilter', args=[self.pk])


@register_search
class FirewallFilterIndex(SearchIndex):
    model = FirewallFilter
    fields = (
        ("name", 100),
        ("device", 200),
        ("comments", 5000),
    )
