from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from dcim.models import Device, Interface
from ipam.fields import IPNetworkField, IPAddressField

from netbox.models import NetBoxModel
from netbox.search import SearchIndex, register_search


################################################################################
# Security Zone
################################################################################

class SecurityZone(NetBoxModel):

    PROTOCOLS_CHOICES = [
        ('all', 'All Protocols'),
        ('bfd', 'Bidirectional Forwarding Detection'),
        ('bgp', 'Border Gateway Protocol'),
        ('dvmrp', 'Distance Vector Multicast Routing Protocol'),
        ('igmp', 'Internet Group Management Protocol'),
        ('ldp', 'Label Distribution Protocol'),
        ('msdp', 'Multicast Source Discovery Protocol'),
        ('nhrp', 'Next Hop Resolution Protocol'),
        ('ospf', 'Open Shortest Path First'),
        ('ospf3', 'Open Shortest Path First version 3'),
        ('pgm', 'Pragmatic General Multicast'),
        ('pim', 'Protocol Independent Multicast'),
        ('rip', 'Routing Information Protocol'),
        ('ripng', 'Routing Information Protocol next generation'),
        ('router-discovry', 'Router Discovery'),
        ('rsvp', 'Resource Reservation Protocol'),
        ('sap', 'Session Announcement Protocol'),
        ('vrrp', 'Virtual Router Redundancy Protocol'),
    ]

    SERVICES_CHOICES = [
        ('all','All System Services'),
        ('any-service','Enable services on entire port range'),
        ('appqoe','APPQOE active probe service'),
        ('bootp','Bootp and dhcp relay-agent service'),
        ('dhcp','Dynamic Host Configuration Protocol'),
        ('dhcpv6','Dynamic Host Configuration Protocol for IPv6'),
        ('dns','DNS service'),
        ('finger','Finger service'),
        ('ftp','FTP service'),
        ('high-availability','High Availability service'),
        ('http','Web management service using HTTP'),
        ('https','Web management service using HTTP secured by SSL'),
        ('ident-reset','Send back TCP RST to IDENT request for port 113'),
        ('ike','Internet Key Exchange'),
        ('lsping','Label Switched Path ping service'),
        ('lsselfping','Label Switched Path self ping service'),
        ('netconf','NETCONF service'),
        ('ntp','Network Time Protocol service'),
        ('ping','Internet Control Message Protocol echo requests'),
        ('r2cp','Radio-Router Control Protocol service'),
        ('reverse-ssh','Reverse SSH service'),
        ('reverse-telnet','Reverse telnet service'),
        ('rlogin','Rlogin service'),
        ('rpm','Real-time performance monitoring'),
        ('rsh','Rsh service'),
        ('snmp','Simple Network Management Protocol service'),
        ('snmp-trap','Simple Network Management Protocol traps'),
        ('ssh','SSH service'),
        ('tcp-encap','Tcp encapsulation service'),
        ('telnet','Telnet service'),
        ('tftp','TFTP service'),
        ('traceroute','Traceroute service'),
        ('webapi-clear-text','Webapi service using http'),
        ('webapi-ssl','Webapi service using HTTP secured by SSL'),
        ('xnm-clear-text','JUNOScript API for unencrypted traffic over TCP'),
        ('xnm-ssl','JUNOScript API service over SSL'),
    ]


    name = models.CharField(
        max_length=64,
        blank=False,
        verbose_name="Name"
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
        verbose_name="Interfaces"
    )

    protocols = ArrayField(
        models.CharField(
            max_length=512,
            choices=PROTOCOLS_CHOICES
        ),
        default=list,
        blank=True,
        verbose_name="Allowed system protocols"
    )

    services = ArrayField(
        models.CharField(
            max_length=512,
            choices=SERVICES_CHOICES
        ),
        default=list,
        blank=True,
        verbose_name="Allowed system services"
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

    def save(self, *args, **kwargs):
        if self.protocols:
            self.protocols.sort()
        if self.services:
            self.services.sort()
        super().save(*args, **kwargs)

    def get_protocols_display(self):
        display_map = dict(SecurityZone.PROTOCOLS_CHOICES)
        return [display_map.get(c, c) for c in self.protocols]

    def get_services_display(self):
        display_map = dict(SecurityZone.SERVICES_CHOICES)
        return [display_map.get(c, c) for c in self.services]


@register_search
class SecurityZoneIndex(SearchIndex):
    model = SecurityZone
    fields = (
        ("name", 100),
        ("device", 200),
        ("description", 300),
        ("comments", 5000),
    )

################################################################################
# Security Address (Address Book)
################################################################################

class SecurityAddress(NetBoxModel):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=64,
        blank=False,
    )

    address = IPNetworkField(
        verbose_name=_('Address'),
        help_text=_('IPv4 or IPv6 address with mask')
    )

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    is_global = models.BooleanField(
        verbose_name=_('Global'),
        default=False,
    )

    security_zone = models.ForeignKey(
        SecurityZone,
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('Security Zone'),
    )

    comments = models.TextField(
        verbose_name=_('Comments'),
        blank=True
    )

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
        ordering = ['device','name']
        constraints = [
            models.CheckConstraint(
                check=(
                    models.Q(is_global=True, security_zone__isnull=True) |
                    models.Q(is_global=False, security_zone__isnull=False)
                ),
                name='unique_security_address_configured'
            ),
            models.UniqueConstraint(
                fields=['name','device','is_global','security_zone'],
                name='unique_security_address'
            )
        ]
        indexes = [
            models.Index(fields=['device','name'], name='idx_security_adress'),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_juniper:securityaddress', args=[self.pk])

    def clean(self):
        super().clean()
        if self.is_global and self.security_zone is not None:
            raise ValidationError("Security Address Book entry can be either Global or per Security Zone.")
        if not self.is_global and self.security_zone is None:
            raise ValidationError("Security Address Book entry can be either Global or per Security Zone.")



@register_search
class SecurityAddressIndex(SearchIndex):
    model = SecurityAddress
    fields = (
        ("name", 100),
        ("device", 200),
        ("comments", 5000),
    )


################################################################################
# Security Address Set (Address Book)
################################################################################

class SecurityAddressSet(NetBoxModel):
    name = models.CharField(
        max_length=64,
        blank=False,
        verbose_name=_('Address Set'),
    )

    address = models.ManyToManyField(
        to="SecurityAddress",
        blank=False,
        verbose_name=_("Addresses"),
    )

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    is_global = models.BooleanField(
        verbose_name=_('Global'),
        default=False,
    )

    security_zone = models.ForeignKey(
        SecurityZone,
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_('Security Zone'),
    )

    comments = models.TextField(
        verbose_name=_('Comments'),
        blank=True
    )

    class Meta:
        verbose_name = _("Address Set")
        verbose_name_plural = _("Address Sets")
        ordering = ['device','name']
        constraints = [
            models.UniqueConstraint(
                fields=['name','device','is_global','security_zone'],
                name='unique_security_address_set'
            )
        ]
        indexes = [
            models.Index(fields=['device','name'], name='idx_security_adress_set'),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_juniper:securityaddressset', args=[self.pk])


@register_search
class SecurityAddressSetIndex(SearchIndex):
    model = SecurityAddressSet
    fields = (
        ("name", 100),
        ("device", 200),
        ("comments", 5000),
    )
