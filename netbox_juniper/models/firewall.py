from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search

#
# Firewall Filter
#

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

#
# Firewall Policer
#

class FirewallPolicer(NetBoxModel):
    name = models.CharField(
        max_length=64,
        blank=False
    )
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.CASCADE,
    )
    bw_limit = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('bandwidth limit (bps)'),
        help_text=_("bandwidth limit - bits per second")
    )
    bw_percent = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('bandwidth percentage'),
        help_text=_("bandwidth percentage")
    )
    burst_limit = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('burst size limit'),
        help_text=_("burst size limit - bytes")
    )
    filter_specific = models.BooleanField(
        default=False,
        verbose_name="Filter Specific?"
    )
    # need to provide future options for forwarding-class, loss-priority, out-of-profile, etc.
    action =  models.CharField(max_length=20,
        blank=False,
        choices=[
            ('discard', 'Discard'),
        ]
    )

    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Firewall Policer")
        verbose_name_plural = _("Firewall Policers")
        ordering = ['device','name']
        constraints = [
            models.UniqueConstraint(
                fields=['device', 'name'],
                name='unique_firewall_policer'
            )
        ]
        indexes = [
            models.Index(fields=['name'], name='idx_firewall_policer_name'),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_juniper:firewallpolicer', args=[self.pk])


@register_search
class FirewallPolicerIndex(SearchIndex):
    model = FirewallPolicer
    fields = (
        ("name", 100),
        ("device", 200),
        ("comments", 5000),
    )
