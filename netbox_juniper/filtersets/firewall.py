import django_filters
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet

from netbox_juniper.models.firewall import *

#
# Firewall Filter
#

class FirewallFilterFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = FirewallFilter
        fields = ('id', 'device', 'name', 'family','comments')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(device__icontains=value)
            | Q(name__icontains=value)
            | Q(family__icontains=value)
            | Q(comments__icontains=value)
        )
        return queryset.filter(qs_filter)

#
# Firewall Policer
#

class FirewallPolicerFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = FirewallPolicer
        fields = ('id', 'device', 'name', 'comments')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(device__icontains=value)
            | Q(name__icontains=value)
            | Q(comments__icontains=value)
        )
        return queryset.filter(qs_filter)
