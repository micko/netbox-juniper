from netbox.api.viewsets import NetBoxModelViewSet

from . serializers import *

from netbox_juniper.models import *
from netbox_juniper.filtersets import *

################################################################################
# Security
################################################################################

class SecurityZoneViewSet(NetBoxModelViewSet):
    queryset = SecurityZone.objects.prefetch_related('tags')
    serializer_class = SecurityZoneSerializer

class SecurityAddressViewSet(NetBoxModelViewSet):
    queryset = SecurityAddress.objects.prefetch_related('tags')
    serializer_class = SecurityAddressSerializer

class SecurityAddressSetViewSet(NetBoxModelViewSet):
    queryset = SecurityAddressSet.objects.prefetch_related('tags')
    serializer_class = SecurityAddressSetSerializer
