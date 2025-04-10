from netbox.api.viewsets import NetBoxModelViewSet

from . serializers import *

from netbox_juniper.models import *
from netbox_juniper.filtersets import *


class FirewallFilterViewSet(NetBoxModelViewSet):
    queryset = FirewallFilter.objects.prefetch_related('tags')
    serializer_class = FirewallFilterSerializer


class FirewallPolicerViewSet(NetBoxModelViewSet):
    queryset = FirewallPolicer.objects.prefetch_related('tags')
    serializer_class = FirewallPolicerSerializer

class SecurityZoneViewSet(NetBoxModelViewSet):
    queryset = SecurityZone.objects.prefetch_related('tags')
    serializer_class = SecurityZoneSerializer
