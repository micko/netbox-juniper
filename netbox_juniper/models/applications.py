from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from dcim.models import Device

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search


################################################################################
# Application
################################################################################

class Application(NetBoxModel):

    APPLICATION_PROTOCOL_CHOICES = [
        ('dns','Domain Name Service'),
        ('ftp','File Transfer Protocol'),
        ('ftp-data','File Transfer Protocol Data Session'),
        ('http','Hypertext Transfer Protocol'),
        ('https','Hypertext Transfer Protocol'),
        ('ignore','Ignore application type'),
        ('ike-esp-nat','IKE/ESP with NAT'),
        ('imap','Internet Mail Access Protocol'),
        ('imaps','Internet Mail Access Protocol Over TLS'),
        ('mgcp-ca','MGCP-CA'),
        ('mgcp-ua','MGCP-UA'),
        ('ms-rpc','Microsoft RPC'),
        ('none','None'),
        ('pop3','Post Office Protocol 3 Protocol'),
        ('pop3s','Post Office Protocol 3 Protocol Over TLS'),
        ('pptp','Point-to-Point Tunneling Protocol'),
        ('q931','Q.931'),
        ('ras','RAS'),
        ('realaudio','RealAudio'),
        ('rsh','Remote Shell'),
        ('rtsp','Real Time Streaming Protocol'),
        ('sccp','Skinny Client Control Protocol'),
        ('sip','Session Initiation Protocol'),
        ('smtp','Simple Mail Transfer Protocol'),
        ('smtps','Simple Mail Transfer Protocol Over TLS'),
        ('sqlnet-v2','Oracle SQL*Net Version 2'),
        ('ssh','Secure Shell Protocol'),
        ('sun-rpc','Sun Microsystems RPC'),
        ('talk','Talk Program'),
        ('telnet','Telnet Protocol'),
        ('tftp','Trivial File Transfer Protocol'),
        ('twamp','Two Way Active Meaurement Protocol'),
    ]

    name = models.CharField(
        max_length=64,
        blank=False,
        verbose_name="Name"
    )

    is_global = models.BooleanField(
        verbose_name=_('Global'),
        default=False,
    )

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    application_protocol = models.CharField(
        max_length=128,
        choices=APPLICATION_PROTOCOL_CHOICES,
        blank=True,
        verbose_name="Application Protocol Type"
    )

    inactivity_timeout = models.CharField(
        max_length=64,
        blank=True,
        verbose_name="Application Inactivity Timeout"
    )

    protocol = models.CharField(
        max_length=64,
        blank=True,
        verbose_name="IP Protocol Type"
    )

    source_port = models.CharField(
        max_length=64,
        blank=True,
        verbose_name="Source Port"
    )

    destination_port = models.CharField(
        max_length=64,
        blank=True,
        verbose_name="Destination Port"
    )

    icmp_code = models.CharField(
        max_length=64,
        blank=True,
        verbose_name="ICMP Code"
    )

    icmp_type = models.CharField(
        max_length=64,
        blank=True,
        verbose_name="ICMP Type"
    )

    icmp6_code = models.CharField(
        max_length=64,
        blank=True,
        verbose_name="ICMPv6 Code"
    )

    icmp6_type = models.CharField(
        max_length=64,
        blank=True,
        verbose_name="ICMPv6 Type"
    )

    description = models.CharField(
        max_length=256,
        blank=True,
        verbose_name="Description",
    )

    comments = models.TextField(
        verbose_name=_('Comments'),
        blank=True
    )

    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")
        ordering = ['name','is_global','device']
        constraints = [
            models.CheckConstraint(
                check=(
                    models.Q(is_global=True, device=True) |
                    models.Q(is_global=False, device__isnull=False)
                ),
                name='unique_application_configured'
            ),
            models.UniqueConstraint(
                fields=['name','device'],
                name='unique_application_name'
            )
        ]
        indexes = [
            models.Index(fields=['name'], name='idx_application_name'),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_juniper:application', args=[self.pk])

    def get_application_protocol_display(self):
        display_map = dict(Application.APPLICATION_PROTOCOL_CHOICES)
        return [display_map.get(c, c) for c in self.application_protocol]


@register_search
class ApplicationIndex(SearchIndex):
    model = Application
    fields = (
        ("name", 100),
        ("device", 200),
        ("description", 300),
        ("comments", 5000),
    )


################################################################################
# Application Set
################################################################################

class ApplicationSet(NetBoxModel):
    name = models.CharField(
        max_length=64,
        blank=False,
        verbose_name=_('Application Set'),
    )

    is_global = models.BooleanField(
        verbose_name=_('Global'),
        default=False,
    )

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    application = models.ManyToManyField(
        to="Application",
        blank=False,
        verbose_name=_("Applications"),
    )

    description = models.CharField(
        max_length=256,
        blank=True,
        verbose_name="Description",
    )

    comments = models.TextField(
        verbose_name=_('Comments'),
        blank=True
    )

    class Meta:
        verbose_name = _("Application Set")
        verbose_name_plural = _("Application Sets")
        ordering = ['name','is_global','device']
        constraints = [
            models.CheckConstraint(
                check=(
                    models.Q(is_global=True, device=True) |
                    models.Q(is_global=False, device__isnull=False)
                ),
                name='unique_application_set_configured'
            ),
            models.UniqueConstraint(
                fields=['name','device'],
                name='unique_application_set_name'
            )
        ]
        indexes = [
            models.Index(fields=['name'], name='idx_application_set_name'),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_juniper:applicationset', args=[self.pk])


@register_search
class ApplicationSetIndex(SearchIndex):
    model = ApplicationSet
    fields = (
        ("name", 100),
        ("device", 200),
        ("description", 300),
        ("comments", 5000),
    )
