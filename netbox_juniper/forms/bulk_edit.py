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

from netbox_juniper.models.applications import *
from netbox_juniper.models.security import *

################################################################################
# Application
################################################################################

class ApplicationBulkEditForm(NetBoxModelBulkEditForm):

    application_protocol = forms.CharField(
        required=False,
    )

    inactivity_timeout = forms.CharField(
        required=False,
    )

    protocol = forms.CharField(
        required=False,
    )

    source_port = forms.CharField(
        required=False,
    )

    destination_port = forms.CharField(
        required=False,
    )

    icmp_code = forms.CharField(
        required=False,
    )

    icmp_type = forms.CharField(
        required=False,
    )

    icmp6_code = forms.CharField(
        required=False,
    )

    icmp6_type = forms.CharField(
        required=False,
    )

    description = forms.CharField(
        required=False,
    )

    comments = CommentField()

    model = Application

    nullable_fields = (
        'application_protocol', 'inactivity_timeout', 'protocol', 'source_port',
        'destination_port', 'icmp_code', 'icmp_type', 'icmp6_code', 'icmp6_type',
        'description','comments',
    )

################################################################################
# Application Set
################################################################################

class ApplicationSetBulkEditForm(NetBoxModelBulkEditForm):

    description = forms.CharField(
        required=False,
    )

    comments = CommentField()

    model = ApplicationSet

    nullable_fields = (
        'device', 'application', 'description','comments',
    )


################################################################################
# Security Zone
################################################################################

class SecurityZoneBulkEditForm(NetBoxModelBulkEditForm):

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

    description = forms.CharField(
        required=False,
    )

    comments = CommentField()

    model = SecurityZone

    nullable_fields = (
        'application_tracking', 'enable_reverse_reroute', 'tcp_rst', 'unidirectional_session_refreshing',
        'comments',
    )

################################################################################
# Security Address (Address Book)
################################################################################

class SecurityAddressBulkEditForm(NetBoxModelBulkEditForm):

    is_global = forms.BooleanField(
        required=False,
    )

    comments = CommentField()

    model = SecurityAddress

    nullable_fields = (
        'is_global', 'security_zone', 'comments',
    )

################################################################################
# Security Address Set (Address Book)
################################################################################

class SecurityAddressSetBulkEditForm(NetBoxModelBulkEditForm):

    is_global = forms.BooleanField(
        required=False,
    )

    comments = CommentField()

    model = SecurityAddressSet

    nullable_fields = (
        'is_global', 'security_zone', 'comments',
    )

