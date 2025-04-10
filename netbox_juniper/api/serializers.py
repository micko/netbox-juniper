from rest_framework.serializers import HyperlinkedIdentityField, ValidationError
from netbox.api.serializers import NetBoxModelSerializer
from netbox_juniper.models import *


#
# Firewall Filter
#

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

#
# Firewall Policer
#

class FirewallPolicerSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='plugins-api:netbox_juniper-api:firewallpolicer-detail'
    )

    class Meta:
        model = FirewallPolicer
        fields = (
            'id', 'url', 'display', 'name', 'device', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'name',
        )

#
# Security Zone
#

class SecurityZoneSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='plugins-api:netbox_juniper-api:securityzone-detail'
    )

    class Meta:
        model = SecurityZone
        fields = (
            'id', 'url', 'display', 'name', 'device', 'interfaces', 'host_inbound_traffic_protocols', 'host_inbound_traffic_services',
            'application_tracking', 'enable_reverse_reroute', 'tcp_rst', 'unidirectional_session_refreshing', 'description', 
            'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'name',
        )
