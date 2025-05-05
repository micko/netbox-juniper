import django_filters
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from django.utils.translation import gettext as _

from utilities.filters import (
    ContentTypeFilter,
    MultiValueCharFilter,
    MultiValueNumberFilter,
    NumericArrayFilter,
    TreeNodeMultipleChoiceFilter,
)

from netbox_juniper.models.security import *

################################################################################
# Security Zone
################################################################################

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

################################################################################
# Security Address (Address Book)
################################################################################


class SecurityAddressFilterSet(NetBoxModelFilterSet):

    address = MultiValueCharFilter(
        method='filter_prefix',
        label=_('Address'),
    )

    class Meta:
        model = SecurityAddress
        fields = ('id', 'device', 'name', 'address', 'is_global', 'security_zone', 'comments')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(device__icontains=value)
            | Q(name__icontains=value)
            | Q(address__icontains=value)
            | Q(security_zone__icontains=value)
            | Q(comments__icontains=value)
        )
        return queryset.filter(qs_filter)

################################################################################
# Security Address Set (Address Book)
################################################################################


class SecurityAddressSetFilterSet(NetBoxModelFilterSet):

    address = MultiValueCharFilter(
        method='filter_prefix',
        label=_('Address'),
    )

    class Meta:
        model = SecurityAddressSet
        fields = ('id', 'device', 'name', 'address', 'is_global', 'security_zone', 'comments')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(device__icontains=value)
            | Q(name__icontains=value)
            | Q(address__icontains=value)
            | Q(security_zone__icontains=value)
            | Q(comments__icontains=value)
        )
        return queryset.filter(qs_filter)

