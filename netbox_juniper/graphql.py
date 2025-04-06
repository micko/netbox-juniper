from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models


class FirewallFilterType(NetBoxObjectType):

    class Meta:
        model = models.FirewallFilter
        fields = '__all__'


class Query(ObjectType):
    firewall_filter = ObjectField(FirewallFilterType)
    firewall_filter_list = ObjectListField(FirewallFilterType)
