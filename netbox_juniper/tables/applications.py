import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import (
    ChoiceFieldColumn,
    NetBoxTable,
    TagColumn,
    ActionsColumn,
)

from netbox_juniper.models.applications import *

################################################################################
# Application
################################################################################

class ApplicationTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
        verbose_name=_("Application Name"),
    )

    device = tables.Column(
        linkify=True,
        verbose_name=_("Device Name"),
    )

    class Meta(NetBoxTable.Meta):
        model = Application
        fields = (
            'pk', 'id',
            'name', 'is_global', 'device', 'application_protocol', 'inactivity_timeout',
            'protocol', 'source_port', 'destination_port', 'icmp_code', 'icmp_type',
            'icmp6_code', 'icmp6_type', 'description',
            'comments', 'actions'
        )
        default_columns = ('name', 'is_global', 'device')


################################################################################
# Application Set
################################################################################

class ApplicationSetTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
        verbose_name=_("Application Set Name"),
    )

    device = tables.Column(
        linkify=True,
        verbose_name=_("Device Name"),
    )

    application = tables.Column(
        linkify=True,
        verbose_name=_("Application Name"),
    )

    class Meta(NetBoxTable.Meta):
        model = ApplicationSet
        fields = (
            'pk', 'id',
            'name', 'is_global', 'device', 'application',
            'comments', 'actions'
        )
        default_columns = ('name', 'is_global', 'device')
