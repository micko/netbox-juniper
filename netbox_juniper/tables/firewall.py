import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import (
    ChoiceFieldColumn,
    NetBoxTable,
    TagColumn,
    ActionsColumn,
)

from netbox_juniper.models import *


class FirewallFilterTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
        verbose_name=_("Filter Name"),
    )
    device = tables.LinkColumn(
        verbose_name=_("Device Name"),
    )
    term_count = tables.Column(
        verbose_name=_("Number of Terms"),
    )

    class Meta(NetBoxTable.Meta):
        model = FirewallFilter
        fields = ('pk', 'id', 'name', 'device', 'family', 'term_count', 'comments', 'actions')
        default_columns = ('name', 'device', 'family', 'term_count')
