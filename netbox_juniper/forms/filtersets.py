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

class ApplicationFilterForm(NetBoxModelFilterSetForm):
    model = Application

    q = forms.CharField(
        required=False,
        label="Search"
    )

    name = forms.CharField(
        max_length=64,
        required=False
    )

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )

    tag = TagFilterField(Application)


################################################################################
# Application Set
################################################################################

class ApplicationSetFilterForm(NetBoxModelFilterSetForm):
    model = ApplicationSet

    q = forms.CharField(
        required=False,
        label="Search"
    )

    name = forms.CharField(
        max_length=64,
        required=False
    )

    application = DynamicModelChoiceField(
        queryset=Application.objects.all(),
        required=False,
    )

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )

    tag = TagFilterField(ApplicationSet)


################################################################################
# Security Zone
################################################################################

class SecurityZoneFilterForm(NetBoxModelFilterSetForm):
    model = SecurityZone

    q = forms.CharField(
        required=False,
        label="Search"
    )

    name = forms.CharField(
        max_length=64,
        required=False
    )

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )

    tag = TagFilterField(SecurityZone)

################################################################################
# Security Address (Address Book)
################################################################################

class SecurityAddressFilterForm(NetBoxModelFilterSetForm):
    model = SecurityAddress

    q = forms.CharField(
        required=False,
        label="Search"
    )

    name = forms.CharField(
        max_length=64,
        required=False
    )

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )

    tag = TagFilterField(SecurityAddress)

################################################################################
# Security Address Set (Address Book)
################################################################################

class SecurityAddressSetFilterForm(NetBoxModelFilterSetForm):
    model = SecurityAddressSet

    q = forms.CharField(
        required=False,
        label="Search"
    )

    name = forms.CharField(
        max_length=64,
        required=False
    )

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )

    tag = TagFilterField(SecurityAddressSet)
