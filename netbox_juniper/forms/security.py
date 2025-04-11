from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.forms import SimpleArrayField
from utilities.forms.fields import (
    DynamicModelChoiceField,
    CSVModelChoiceField,
    CSVModelMultipleChoiceField,
    DynamicModelMultipleChoiceField,
    TagFilterField,
    CSVChoiceField,
    CommentField,
)
from utilities.forms.rendering import FieldSet
from dcim.models import Device, Interface
from ipam.fields import IPNetworkField, IPAddressField
from netbox.forms import (
    NetBoxModelForm,
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
)

from netbox_juniper.models.security import *

#
# Security Zone
#

class SecurityZoneForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        label=_('Device'),
        queryset=Device.objects.all(),
        required=True,
    )
    interfaces = DynamicModelMultipleChoiceField(
        label=_('Interfaces'),
        queryset=Interface.objects.all(),
        required=False,
        query_params={
            'device_id': '$device',
        }
    )
    host_inbound_traffic_protocols = forms.MultipleChoiceField(
        choices=SecurityZoneHostInboundTrafficProtocolsChoices,
        label=_('Protocols'),
        widget=forms.SelectMultiple,
        required=False,
        help_text=_('Protocol type of incoming traffic to accept')
    )
    host_inbound_traffic_services = forms.MultipleChoiceField( 
        choices=SecurityZoneHostInboundTrafficServicesChoices,
        label=_('Services'),
        widget=forms.SelectMultiple,
        required=False,
        help_text=_('Type of incoming system-service traffic to accept')
    )

    comments = CommentField()

    class Meta:
        model = SecurityZone
        fields = (
            'name', 'device', 'interfaces', 'host_inbound_traffic_protocols', 'host_inbound_traffic_services',
            'application_tracking', 'enable_reverse_reroute', 'tcp_rst', 'unidirectional_session_refreshing',
            'description', 'comments', 'tags'
        )


class SecurityZoneFilterForm(NetBoxModelFilterSetForm):
    model = SecurityZone

    q = forms.CharField(required=False, label="Search")

    name = forms.CharField(max_length=64, required=False)

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )

    tag = TagFilterField(SecurityZone)


class SecurityZoneBulkEditForm(NetBoxModelBulkEditForm):
    model = SecurityZone

    name = forms.CharField(max_length=64, required=False)
    device = DynamicModelChoiceField(
        label=_("Device"),
        queryset=Device.objects.all(),
        required=True,
    )
    interfaces = DynamicModelMultipleChoiceField(
        label=_("Interfaces"),
        queryset=Interface.objects.all(),
        required=False,
    )

    application_tracking = forms.BooleanField(
        required=False,
    )
    enable_reverse_reroute = forms.BooleanField(
        required=False,
    )
    tcp_rst = forms.BooleanField(
        required=False,
    )
    unidirectional_session_refreshing = forms.BooleanField(
        required=False,
    )
    # remaining
    description = forms.CharField(
        required=False,
    )
    comments = CommentField()


class SecurityZoneImportForm(NetBoxModelImportForm):
    device = CSVModelChoiceField(
        label=_('Device'),
        queryset=Device.objects.all(),
        required=True,
        to_field_name="device",
        help_text=_("Device"),
    )
    interfaces = CSVModelMultipleChoiceField(
        label=_('Interfaces'),
        queryset=Interface.objects.all(),
        required=False,
        to_field_name="interfaces",
        help_text=_("Interfaces"),
    )


    class Meta:
        model = SecurityZone
        fields = (
            'name', 'device', 'interfaces', 'host_inbound_traffic_protocols', 'host_inbound_traffic_services',
            'application_tracking', 'enable_reverse_reroute', 'tcp_rst', 'unidirectional_session_refreshing',
            'description', 'comments', 'tags'
        )

#
# Address Book
#

class AddressBookAddressForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = AddressBookAddress
        fields = (
            'device','name','address','is_global','security_zone',
            'comments', 'tags'
        )

class AddressBookAddressFilterForm(NetBoxModelFilterSetForm):
    model = SecurityZone

    q = forms.CharField(required=False, label="Search")

    name = forms.CharField(max_length=64, required=False)

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )

    tag = TagFilterField(AddressBookAddress)


class AddressBookAddressBulkEditForm(NetBoxModelBulkEditForm):
    model = AddressBookAddress

    name = forms.CharField(
        max_length=64,
        required=False
    )
    device = DynamicModelChoiceField(
        label=_("Device"),
        queryset=Device.objects.all(),
        required=True,
    )
#    address = IPNetworkField(
#        queryset=AddressBookAddress.objects.all(),
#        required=False,
#    )
    is_global = forms.BooleanField(
        required=False,
    )
    security_zone = DynamicModelChoiceField(
        label=_("Security Zone"),
        queryset=SecurityZone.objects.all(),
        required=False,
    )
    comments = CommentField()

class AddressBookAddressImportForm(NetBoxModelImportForm):
    device = CSVModelChoiceField(
        label=_('Device'),
        queryset=Device.objects.all(),
        required=True,
        to_field_name="device",
        help_text=_("Device Name"),
    )
    security_zone = CSVModelMultipleChoiceField(
        label=_('SecurityZone'),
        queryset=SecurityZone.objects.all(),
        required=False,
        to_field_name="security_zone",
        help_text=_("Security Zone"),
    )

    class Meta:
        model = AddressBookAddress
        fields = (
            'device', 'name', 'address','is_global', 'security_zone',
            'comments', 'tags'
        )
