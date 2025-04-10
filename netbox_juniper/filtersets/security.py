import django_filters
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet

from netbox_juniper.models.security import *

#
# Security Zone
#

class SecurityZoneFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = SecurityZone
        fields = ('id', 'name', 'device', 'interfaces', 'description', 'comments')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(device__icontains=value)
            | Q(interfces__icontains=value)
            | Q(description__icontains=value)
            | Q(comments__icontains=value)
        )
        return queryset.filter(qs_filter)
