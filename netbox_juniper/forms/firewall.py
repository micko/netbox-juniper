from django import forms
from django.utils.translation import gettext_lazy as _
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
from dcim.models import Device
from netbox.forms import (
    NetBoxModelForm,
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
)

from netbox_juniper.models.firewall import *

#
# Firewall Filter
#

class FirewallFilterForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=True,
    )
    comments = CommentField()

    class Meta:
        model = FirewallFilter
        fields = ('device', 'name', 'family', 'comments', 'tags')


class FirewallFilterFilterForm(NetBoxModelFilterSetForm):
    q = forms.CharField(required=False, label="Search")
    device = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    name = forms.CharField(max_length=64, required=False)
    family = forms.CharField(max_length=64, required=False)

    tag = TagFilterField(FirewallFilter)

    model = FirewallFilter


class FirewallFilterBulkEditForm(NetBoxModelBulkEditForm):
    device = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    name = forms.CharField(max_length=64, required=False)
    family = forms.CharField(max_length=64, required=False)

    model = FirewallFilter


class FirewallFilterImportForm(NetBoxModelImportForm):
    device = CSVModelChoiceField(
        queryset=Device.objects.all(),
        required=True,
        to_field_name="name",
        help_text=_("Device"),
    )

    family = CSVChoiceField(
        choices=[
            ('inet', 'IPv4'),
            ('inet6', 'IPv6'),
            ('ethernet-switching', 'Layer 2'),
        ],
        help_text=_("Family"),
    )

    class Meta:
        model = FirewallFilter
        fields = ("device", "name", "family", "tags")


#
# Firewall Policer
#

class FirewallPolicerForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=True,
    )
    comments = CommentField()

    class Meta:
        model = FirewallPolicer
        fields = ('device', 'name', 'bw_limit', 'bw_percent', 'burst_limit', 'comments', 'tags')


class FirewallPolicerFilterForm(NetBoxModelFilterSetForm):
    q = forms.CharField(required=False, label="Search")
    device = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    name = forms.CharField(max_length=64, required=False)

    tag = TagFilterField(FirewallFilter)

    model = FirewallPolicer


class FirewallPolicerBulkEditForm(NetBoxModelBulkEditForm):
    device = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    name = forms.CharField(max_length=64, required=False)

    model = FirewallPolicer


class FirewallPolicerImportForm(NetBoxModelImportForm):
    device = CSVModelChoiceField(
        queryset=Device.objects.all(),
        required=True,
        to_field_name="name",
        help_text=_("Device"),
    )

    class Meta:
        model = FirewallPolicer
        fields = ("device", "name", "bw_limit", "bw_percent", "burst_limit", "tags")
