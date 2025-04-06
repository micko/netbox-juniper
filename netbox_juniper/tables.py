import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import FirewallFilter

class FirewallFilterTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    device = tables.LinkColumn()

    class Meta(NetBoxTable.Meta):
        model = FirewallFilter
        fields = ('pk', 'id', 'name', 'device', 'family', 'description', 'actions')
        default_columns = ('name', 'device', 'family', 'description')
