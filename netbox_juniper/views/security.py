from netbox.views import generic
from django.db.models import Count

from netbox_juniper.filtersets.security import *
from netbox_juniper.forms.security import *
from netbox_juniper.models.security import *
from netbox_juniper.tables.security import *

#
# Security Zone
#

class SecurityZoneView(generic.ObjectView):
    queryset = SecurityZone.objects.all()
    table = SecurityZoneTable


class SecurityZoneListView(generic.ObjectListView):
    queryset = SecurityZone.objects.all()
    filterset = SecurityZoneFilterSet
    filterset_form = SecurityZoneFilterForm
    table = SecurityZoneTable


class SecurityZoneEditView(generic.ObjectEditView):
    queryset = SecurityZone.objects.all()
    form = SecurityZoneForm


class SecurityZoneBulkEditView(generic.BulkEditView):
    queryset = SecurityZone.objects.all()
    filterset = SecurityZoneFilterSet
    table = SecurityZoneTable
    form = SecurityZoneBulkEditForm


class SecurityZoneDeleteView(generic.ObjectDeleteView):
    queryset = SecurityZone.objects.all()
    default_return_url = 'plugins:netbox_juniper:securityzone_list'


class SecurityZoneBulkDeleteView(generic.BulkDeleteView):
    queryset = SecurityZone.objects.all()
    table = SecurityZoneTable


class SecurityZoneBulkImportView(generic.BulkImportView):
    queryset = SecurityZone.objects.all()
    model_form = SecurityZoneImportForm
