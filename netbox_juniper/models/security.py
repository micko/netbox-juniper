from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from utilities.choices import ChoiceSet

from dcim.models import Device, Interface
from ipam.fields import IPNetworkField, IPAddressField

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
        ('bgp','Border Gateway Protocol'),
        ('dvmrp','Distance Vector Multicast Routing Protocol'),
        ('igmp','Internet Group Management Protocol'),
        ('ldp','Label Distribution Protocol'),
        ('msdp','Multicast Source Discovery Protocol'),
        ('nhrp','Next Hop Resolution Protocol'),
        ('ospf','Open Shortest Path First'),
        ('ospf3','Open Shortest Path First version 3'),
        ('pgm','Pragmatic General Multicast'),
        ('pim','Protocol Independent Multicast'),
        ('rip','Routing Information Protocol'),
        ('ripng','Routing Information Protocol next generation'),
        ('router-discovery','Router Discovery'),
        ('rsvp','Resource Reservation Protocol'),
        ('sap','Session Announcement Protocol'),
        ('vrrp','Virtual Router Redundancy Protocol'),
    ]


#
# Seecurity Zone - host-inbound-traffic services
#

class SecurityZoneHostInboundTrafficServicesChoices(ChoiceSet):
    key = 'SecurityZone.host_inbound_traffic_services'

    CHOICES = [
        ('all','All System Services'),
        ('any-service','Enable services on entire port range'),
        ('appqoe','APPQOE active probe service'),
        ('bootp','Bootp and dhcp relay-agent service'),
        ('dhcp','Dynamic Host Configuration Protocol'),
        ('dhcpv6','Enable Dynamic Host Configuration Protocol for IPv6'),
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
        ('r2cp','Enable Radio-Router Control Protocol service'),
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
        models.CharField(max_length=512, blank=True, choices=SecurityZoneHostInboundTrafficProtocolsChoices),
        default=list,
        blank=True,
    )
    host_inbound_traffic_services = ArrayField(
        models.CharField(max_length=512, blank=True, choices=SecurityZoneHostInboundTrafficServicesChoices),
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

#
# Address Book - Address
#

class AddressBookAddress(NetBoxModel):
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    name = models.CharField(
        verbose_name=_('Address Name'),
        max_length=64,
        blank=False,
    )
    address = IPNetworkField(
        verbose_name=_('Address'),
        help_text=_('IPv4 or IPv6 address with mask')
    )
    is_global = models.BooleanField(
        default=False,
        verbose_name=_('Global'),
    )
    security_zone = models.ForeignKey(
        SecurityZone,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
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
            models.UniqueConstraint(
                fields=['device','name','is_global','security_zone'],
                name='unique_security_addressbook_address'
            )
        ]
        indexes = [
            models.Index(fields=['device','name'], name='idx_security_adressbook'),
        ] 

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('plugins:netbox_juniper:addressbookaddress', args=[self.pk])

@register_search
class AddressBookAddressIndex(SearchIndex):
    model = AddressBookAddress
    fields = (
        ("device", 100),
        ("name", 100),
        ("address", 300),
        ("comments", 5000),
    )


#
# Address Book - Address Set
#

class AddressBookAddressSet(NetBoxModel):
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    name = models.CharField(
        verbose_name=_('Address Set'),
        max_length=64,
        blank=False,
    )
    address = models.ManyToManyField(
        AddressBookAddress,
        blank=False,
        verbose_name=_('Addresses'),
        help_text=_('Addresses belonging to this address set')
    )
    is_global = models.BooleanField(
        default=False,
        verbose_name=_('Global'),
    )   
    security_zone = models.ForeignKey(
        SecurityZone,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
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
                fields=['device','name','is_global','security_zone'],
                name='unique_security_addressbook_address_set'
            )
        ]
        indexes = [
            models.Index(fields=['device','name'], name='idx_security_address_set'),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_juniper:addressbookaddressset', args=[self.pk])

@register_search
class AddressBookAddressSetIndex(SearchIndex):
    model = AddressBookAddressSet
    fields = (
        ("device", 100),
        ("name", 100),
        ("address", 300),
        ("comments", 5000),
    )
