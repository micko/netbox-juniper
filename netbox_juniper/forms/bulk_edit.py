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

