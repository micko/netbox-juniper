from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from . serializers import FirewallFilterSerializer


class FirewallFilterViewSet(NetBoxModelViewSet):
    queryset = models.FirewallFilter.objects.prefetch_related('tags')
    serializer_class = FirewallFilterSerializer
