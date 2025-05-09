from netbox.api.viewsets import NetBoxModelViewSet

from . serializers import *

from netbox_juniper.models import *
from netbox_juniper.filtersets import *

################################################################################
# Applications
################################################################################

class ApplicationViewSet(NetBoxModelViewSet):
    queryset = Application.objects.prefetch_related('tags')
    serializer_class = ApplicationSerializer

class ApplicationSetViewSet(NetBoxModelViewSet):
    queryset = ApplicationSet.objects.prefetch_related('application','tags')
    serializer_class = ApplicationSetSerializer

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
