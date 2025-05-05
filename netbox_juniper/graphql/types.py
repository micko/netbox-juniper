from typing import Annotated, List

import strawberry
import strawberry_django

from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.scalars import BigInt
from dcim.graphql.types import DeviceType, InterfaceType
from ipam.graphql.types import IPAddressType, PrefixType

from netbox_juniper.models import *

from . filters import *

################################################################################
# Security Zone
################################################################################

@strawberry_django.type(SecurityZone, fields="__all__", filters=SecurityZoneFilter)
class SecurityZoneType(NetBoxObjectType):
    name: str
    device: Annotated["DeviceType", strawberry.lazy("dcim.graphql.types")] | None
    interfaces: List[
        Annotated["InterfaceType", strawberry.lazy('dcim.graphql.types')]
    ] | None
    protocols: List[str] | None
    application_tracking: bool | None
    enable_reverse_reroute: bool | None
    tcp_rst: bool | None
    unidirectional_session_refreshing: bool | None
    description: str | None

################################################################################
# Security Address
################################################################################

@strawberry_django.type(SecurityAddress, fields="__all__", filters=SecurityAddressFilter)
class SecurityAddressType(NetBoxObjectType):
    name: str
    address: Annotated["PrefixType", strawberry.lazy("ipam.graphql.types")]
    device: Annotated["DeviceType", strawberry.lazy("dcim.graphql.types")] | None
    is_global: bool | None
    security_zone: Annotated["SecurityZoneType", strawberry.lazy("netbox_juniper.graphql.types")] | None


################################################################################
# Security Address Set
################################################################################

@strawberry_django.type(SecurityAddressSet, fields="__all__", filters=SecurityAddressSetFilter)
class SecurityAddressSetType(NetBoxObjectType):
    name: str
    address: Annotated["SecurityAddressType", strawberry.lazy("netbox_juniper.graphql.types")] | None
    device: Annotated["DeviceType", strawberry.lazy("dcim.graphql.types")] | None
    is_global: bool | None
    security_zone: Annotated["SecurityZoneType", strawberry.lazy("netbox_juniper.graphql.types")] | None
