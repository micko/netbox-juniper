from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from .. models import FirewallFilter


class FirewallFilterSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_juniper-api:firewallfilter-detail'
    )

    class Meta:
        model = FirewallFilter
        fields = ('id', 'url', 'device', 'name', 'family', 'description', 'tags', 'created', 'last_updated')


class NestedFirewallFilterSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_juniper-api:firewallfilter-detail'
    )

    class Meta:
        model = FirewallFilter
        fields = ('id', 'device', 'name', 'family', 'description')
