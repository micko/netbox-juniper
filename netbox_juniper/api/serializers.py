from rest_framework.serializers import HyperlinkedIdentityField, ValidationError
from netbox.api.serializers import NetBoxModelSerializer
from netbox_juniper.models import *


################################################################################
# Application
################################################################################

class ApplicationSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='plugins-api:netbox_juniper-api:application-detail'
    )

    class Meta:
        model = Application
        fields = (
            'id', 'url', 'display', 'name', 'is_global', 'device', 'application_protocol',
            'inactivity_timeout', 'protocol', 'source_port', 'destination_port',
            'icmp_code', 'icmp_type', 'icmp6_code', 'icmp6_type', 'description',
            'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'name',
        )

################################################################################
# Application Set
################################################################################

class ApplicationSetSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='plugins-api:netbox_juniper-api:applicationset-detail'
    )

    class Meta:
        model = ApplicationSet
        fields = (
            'id', 'url', 'display', 'name', 'is_global', 'device', 'application',
            'description', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'name',
        )

################################################################################
# Security Zone
################################################################################

class SecurityZoneSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='plugins-api:netbox_juniper-api:securityzone-detail'
    )

    class Meta:
        model = SecurityZone
        fields = (
            'id', 'url', 'display', 'name', 'device', 'interfaces', 'protocols', 'services', 'application_tracking',
            'enable_reverse_reroute', 'tcp_rst', 'unidirectional_session_refreshing', 'description', 
            'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'name',
        )

################################################################################
# Security Address (Address Book)
################################################################################

class SecurityAddressSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='plugins-api:netbox_juniper-api:securityaddress-detail'
    )

    class Meta:
        model = SecurityAddress
        fields = (
            'id', 'url', 'display', 'device', 'name', 'address', 'is_global', 'security_zone',
            'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'device', 'name',
        )

################################################################################
# Security Address Set (Address Book)
################################################################################

class SecurityAddressSetSerializer(NetBoxModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='plugins-api:netbox_juniper-api:securityaddressset-detail'
    )

    class Meta:
        model = SecurityAddressSet
        fields = (
            'id', 'url', 'display', 'device', 'name', 'address', 'is_global', 'security_zone',
            'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )
        brief_fields = (
            'id', 'url', 'display', 'device', 'name',
        )
