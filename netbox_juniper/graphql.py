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


class Query(ObjectType):
    firewallfilter = ObjectField(FirewallFilterType)
    firewallfilter_list = ObjectListField(FirewallFilterType)

    firewallpolicer = ObjectField(FirewallPolicerType)
    firewallpolicer_list = ObjectListField(FirewallPolicerType)


schema = Query
