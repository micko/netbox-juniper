from rest_framework.serializers import HyperlinkedIdentityField, ValidationError
from netbox.api.serializers import NetBoxModelSerializer
from netbox_juniper.models import *


class FirewallFilterSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='plugins-api:netbox_juniper-api:firewallfilter-detail'
    )

    class Meta:
        model = FirewallFilter
        fields = (
            'id', 'url', 'display', 'name', 'device', 'family', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'name',
        )
