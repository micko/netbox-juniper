import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _
from netbox.filtersets import NetBoxModelFilterSet
from utilities.filters import MultiValueCharFilter

from netbox_juniper.models import *


class FirewallFilterFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = FirewallFilter
        fields = ('id', 'device', 'name', 'family')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
