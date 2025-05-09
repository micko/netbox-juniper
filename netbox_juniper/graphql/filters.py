from typing import Annotated

import strawberry
import strawberry_django
from strawberry.scalars import ID
from strawberry_django import FilterLookup

from netbox.graphql.filter_mixins import NetBoxModelFilterMixin
from dcim.graphql.filters import DeviceFilter, InterfaceFilter
from ipam.graphql.filters import IPAddressFilter, PrefixFilter

from netbox_juniper.models import *

################################################################################
# Application
################################################################################

@strawberry_django.filter(Application, lookups=True)
class ApplicationFilter(NetBoxModelFilterMixin):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    is_global: FilterLookup[bool] | None = strawberry_django.filter_field()
    device: (
        Annotated["DeviceFilter", strawberry.lazy("dcim.graphql.filters")]
        | None
    ) = strawberry_django.filter_field()
    application_protocol: FilterLookup[str] | None = strawberry_django.filter_field()
    inactivity_timeout: FilterLookup[str] | None = strawberry_django.filter_field()
    protocol: FilterLookup[str] | None = strawberry_django.filter_field()
    source_port: FilterLookup[str] | None = strawberry_django.filter_field()
    destination_port: FilterLookup[str] | None = strawberry_django.filter_field()
    icmp_code: FilterLookup[str] | None = strawberry_django.filter_field()
    icmp_type: FilterLookup[str] | None = strawberry_django.filter_field()
    icmp6_code: FilterLookup[str] | None = strawberry_django.filter_field()
    icmp6_type: FilterLookup[str] | None = strawberry_django.filter_field()
    description: FilterLookup[str] | None = strawberry_django.filter_field()

################################################################################
# Application Set
################################################################################

@strawberry_django.filter(ApplicationSet, lookups=True)
class ApplicationSetFilter(NetBoxModelFilterMixin):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    is_global: FilterLookup[bool] | None = strawberry_django.filter_field()
    device: (
        Annotated["DeviceFilter", strawberry.lazy("dcim.graphql.filters")]
        | None
    ) = strawberry_django.filter_field()
    application: (
        Annotated['ApplicationFilter', strawberry.lazy('netbox_juniper.graphql.filters')]
        | None
    ) = strawberry_django.filter_field()
    description: FilterLookup[str] | None = strawberry_django.filter_field()

################################################################################
# Security Zone
################################################################################

@strawberry_django.filter(SecurityZone, lookups=True)
class SecurityZoneFilter(NetBoxModelFilterMixin):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    device: (
        Annotated["DeviceFilter", strawberry.lazy("dcim.graphql.filters")]
        | None
    ) = strawberry_django.filter_field()
    interfaces: (
        Annotated["InterfaceFilter", strawberry.lazy('dcim.graphql.filters')]
        | None
    ) = strawberry_django.filter_field()
    protocols: FilterLookup[str] | None = strawberry_django.filter_field()
    services: FilterLookup[str] | None = strawberry_django.filter_field()
    application_tracking: FilterLookup[bool] | None = strawberry_django.filter_field()
    enable_reverse_reroute: FilterLookup[bool] | None = strawberry_django.filter_field()
    tcp_rst: FilterLookup[bool] | None = strawberry_django.filter_field()
    unidirectional_session_refreshing: FilterLookup[bool] | None = strawberry_django.filter_field()
    description: FilterLookup[str] | None = strawberry_django.filter_field()

################################################################################
# Security Address
################################################################################

@strawberry_django.filter(SecurityAddress, lookups=True)
class SecurityAddressFilter(NetBoxModelFilterMixin):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    address: (
        Annotated['PrefixFilter', strawberry.lazy('ipam.graphql.filters')]
        | None
    ) = strawberry_django.filter_field()
    device: (
        Annotated["DeviceFilter", strawberry.lazy("dcim.graphql.filters")]
        | None
    ) = strawberry_django.filter_field()
    is_global: FilterLookup[bool] | None = strawberry_django.filter_field()
    security_zone: (
        Annotated["SecurityZoneFilter", strawberry.lazy("netbox_juniper.graphql.filters")]
        | None
    ) = strawberry_django.filter_field()

################################################################################
# Security Address Set
################################################################################

@strawberry_django.filter(SecurityAddressSet, lookups=True)
class SecurityAddressSetFilter(NetBoxModelFilterMixin):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    address: (
        Annotated['SecurityAddressFilter', strawberry.lazy('netbox_juniper.graphql.filters')]
        | None 
    ) = strawberry_django.filter_field()
    device: (
        Annotated["DeviceFilter", strawberry.lazy("dcim.graphql.filters")]
        | None
    ) = strawberry_django.filter_field()
    is_global: FilterLookup[bool] | None = strawberry_django.filter_field()
    security_zone: (
        Annotated["SecurityZoneFilter", strawberry.lazy("netbox_juniper.graphql.filters")]
        | None
    ) = strawberry_django.filter_field()

