from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from dcim.models import Device
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from . models import FirewallFilter


class FirewallFilterForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        queryset=Device.objects.all()
    )

    class Meta:
        model = FirewallFilter
        fields = ('device', 'name', 'family', 'description', 'tags')


class FirewallFilterFilterForm(NetBoxModelFilterSetForm):
    model = FirewallFilter
    device = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )

