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
