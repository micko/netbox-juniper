from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from utilities.choices import ChoiceSet

from dcim.models import Device, Interface

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search




#
# Seecurity Zone - host-inbound-traffic protocols
#

class SecurityZoneHostInboundTrafficProtocolsChoices(ChoiceSet):
    key = 'SecurityZone.host_inbound_traffic_protocols'

    CHOICES = [
        ('all','All Protocols'),
        ('bfd','Bidirectional Forwarding Detection'),
    ]


#
# Seecurity Zone - host-inbound-traffic services
#

class SecurityZoneHostInboundTrafficServicesChoices(ChoiceSet):
    key = 'SecurityZone.host_inbound_traffic_services'

    CHOICES = [
        ('all','All System Services'),
        ('any_service','Enable services on entire port range'),
    ]


#
# Security Zone
#

class SecurityZone(NetBoxModel):
    name = models.CharField(
        max_length=64,
        blank=False,
    )
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    interfaces = models.ManyToManyField(
        Interface,
        blank=True,
        related_name='security_zone_interfaces'
    )

    host_inbound_traffic_protocols = ArrayField(
        models.CharField(max_length=256, blank=True, choices=SecurityZoneHostInboundTrafficProtocolsChoices),
        default=list,
        blank=True,
    )
    host_inbound_traffic_services = ArrayField(
        models.CharField(max_length=256, blank=True, choices=SecurityZoneHostInboundTrafficServicesChoices),
        default=list,
        blank=True,
    )
    application_tracking = models.BooleanField(
        default=False,
        verbose_name="Application Tracking"
    )
    enable_reverse_reroute = models.BooleanField(
        default=False,
        verbose_name="Enable Reverse route lookup"
    )
    tcp_rst = models.BooleanField(
        default=False,
        verbose_name="Send RST for NON-SYN packets"
    )
    unidirectional_session_refreshing = models.BooleanField(
        default=False,
        verbose_name="Enable unidirectional session refreshing"
    )
    # remaining
    description = models.CharField(
        max_length=256,
        blank=True,
        verbose_name="Description",
    )
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Security Zone")
        verbose_name_plural = _("Security Zones")
        ordering = ['device','name']
        constraints = [
            models.UniqueConstraint(
                fields=['device','name'],
                name='unique_security_zone'
            )
        ]
        indexes = [
            models.Index(fields=['name'], name='idx_security_zone_name'),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_juniper:securityzone', args=[self.pk])


@register_search
class SecurityZoneIndex(SearchIndex):
    model = SecurityZone
    fields = (
        ("name", 100),
        ("device", 200),
        ("description", 300),
        ("comments", 5000),
    )
