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

################################################################################
# Security Zone
################################################################################

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
            'name', 'device', 'interfaces', 'protocols', 'services', 'application_tracking',
            'enable_reverse_reroute', 'tcp_rst', 'unidirectional_session_refreshing',
            'description', 'comments', 'tags'
        )

################################################################################
# Security Address (Address Book)
################################################################################

class SecurityAddressImportForm(NetBoxModelImportForm):
    device = CSVModelChoiceField(
        label=_('Device'),
        queryset=Device.objects.all(),
        required=True,
        to_field_name="device",
        help_text=_("Device Name"),
    )
    security_zone = CSVModelMultipleChoiceField(
        label=_('Zone'),
        queryset=SecurityZone.objects.all(),
        required=False,
        to_field_name="security_zone",
        help_text=_("Security Zone"),
    )

    class Meta:
        model = SecurityAddress
        fields = (
            'device', 'name', 'address','is_global', 'security_zone',
            'comments', 'tags'
        )

################################################################################
# Security Address Set (Address Book)
################################################################################

class SecurityAddressSetImportForm(NetBoxModelImportForm):
    device = CSVModelChoiceField(
        label=_('Device'),
        queryset=Device.objects.all(),
        required=True,
        to_field_name="device",
        help_text=_("Device Name"),
    )
    security_zone = CSVModelMultipleChoiceField(
        label=_('Zone'),
        queryset=SecurityZone.objects.all(),
        required=False,
        to_field_name="security_zone",
        help_text=_("Security Zone"),
    )

    address = CSVModelChoiceField(
        label=_('Address'),
        queryset=SecurityAddress.objects.all(),
        required=True,
        to_field_name="address",
        help_text=_("Address"),
    )

    class Meta:
        model = SecurityAddressSet
        fields = (
            'device', 'name', 'address','is_global', 'security_zone',
            'comments', 'tags'
        )

