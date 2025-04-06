from netbox.filtersets import NetBoxModelFilterSet
from . models import FirewallFilter


class FirewallFilterFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = FirewallFilter
        fields = ('id', 'device', 'name', 'family')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
