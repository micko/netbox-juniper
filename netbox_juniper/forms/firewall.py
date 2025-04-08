from django import forms
from django.utils.translation import gettext_lazy as _
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.rendering import FieldSet
from dcim.models import Device
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm

from netbox_juniper.models import *


class FirewallFilterForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=True,
    )
    comments = CommentField()

    class Meta:
        model = FirewallFilter
        fields = ('device', 'name', 'family', 'comments', 'tags')
