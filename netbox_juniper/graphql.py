from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField

from netbox_juniper.models import *
from netbox_juniper.filtersets import *


#
# Firewall Filter
#

class FirewallFilterType(NetBoxObjectType):

    class Meta:
        model = FirewallFilter
        fields = '__all__'

#
# Firewall Policer
#

class FirewallPolicerType(NetBoxObjectType):

    class Meta:
        model = FirewallPolicer
        fields = '__all__'

#
# Security Zone
#

class SecurityZoneType(NetBoxObjectType):

    class Meta:
        model = SecurityZone
        fields = '__all__'


#
# Query
#

class Query(ObjectType):
    firewallfilter = ObjectField(FirewallFilterType)
    firewallfilter_list = ObjectListField(FirewallFilterType)

    firewallpolicer = ObjectField(FirewallPolicerType)
    firewallpolicer_list = ObjectListField(FirewallPolicerType)

    securityzone = ObjectField(SecurityZoneType)
    securityzone_list = ObjectListField(SecurityZoneType)

schema = Query
