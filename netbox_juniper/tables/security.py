import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import (
    ChoiceFieldColumn,
    NetBoxTable,
    TagColumn,
    ActionsColumn,
)

from netbox_juniper.models.security import *

#
# Security Zone
#

class SecurityZoneTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
        verbose_name=_("Security Zone"),
    )
    device = tables.Column(
        linkify=True,
        verbose_name=_("Device Name"),
    )

    class Meta(NetBoxTable.Meta):
        model = SecurityZone
        fields = (
            'pk', 'id',
            'name', 'device', 'interfaces',
            'application_tracking', 'enable_reverse_reroute', 'tcp_rst',
            'unidirectional_session_refreshing', 'description', 
            'comments', 'actions'
        )
        default_columns = ('name', 'device', 'interfaces', 'description')

#
# Address Book - Address
#

class AddressBookAddressTable(NetBoxTable):
    device = tables.Column(
        linkify=True,
        verbose_name=_("Device Name"),
    )
    name = tables.Column(
        linkify=True,
        verbose_name=_("Address Name"),
    )
    security_zone = tables.Column(
        linkify=True,
        verbose_name=_("Security Zone"),
    )

    class Meta(NetBoxTable.Meta):
        model = AddressBookAddress
        fields = (
            'pk', 'id',
            'device', 'name', 'address', 'is_global', 'security_zone',
            'comments', 'actions'
        )
        default_columns = ('device', 'name', 'address', 'is_global','security_zone')


