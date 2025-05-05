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
    protocols = forms.MultipleChoiceField(
        choices=SecurityZone.PROTOCOLS_CHOICES,
        label=_('Protocols'),
        widget=forms.SelectMultiple,
        required=False,
        help_text=_('Protocol type of incoming traffic to accept')
    )
    services = forms.MultipleChoiceField( 
        choices=SecurityZone.SERVICES_CHOICES,
        label=_('Services'),
        widget=forms.SelectMultiple,
        required=False,
        help_text=_('Type of incoming system-service traffic to accept')
    )

    comments = CommentField()

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

class SecurityAddressForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=True,
        label=_('Device')
    )

    name = forms.CharField(
        max_length=64,
        required=True,
        label=_('Name')
    )

    is_global = forms.BooleanField(
        required=False,
    )

    security_zone = DynamicModelChoiceField(
        queryset=SecurityZone.objects.all(),
        required=False,
        label=_('Security Zone')
    )

    comments = CommentField()

    class Meta:
        model = SecurityAddress
        fields = (
            'device','name','address','is_global','security_zone',
            'comments', 'tags'
        )


################################################################################
# Security Address Set (Address Book)
################################################################################

class SecurityAddressSetForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=True,
        label=_('Device')
    )

    name = forms.CharField(
        max_length=64,
        required=True,
        label=_('Name')
    )

    address = DynamicModelMultipleChoiceField(
        label=_('Address'),
        queryset=SecurityAddress.objects.all(),
        required=False,
        query_params={
            'device_id': '$device',
        }
    )

    is_global = forms.BooleanField(
        required=False,
    )

    security_zone = DynamicModelChoiceField(
        queryset=SecurityZone.objects.all(),
        required=False,
        label=_('Security Zone')
    )

    comments = CommentField()

    class Meta:
        model = SecurityAddressSet
        fields = (
            'device','name','address','is_global','security_zone',
            'comments', 'tags'
        )
