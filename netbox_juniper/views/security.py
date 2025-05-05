from netbox.views import generic
from django.db.models import Count

from netbox_juniper.filtersets.security import *
from netbox_juniper.forms import *
from netbox_juniper.models.security import *
from netbox_juniper.tables.security import *

################################################################################
# Security Zone
################################################################################

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


################################################################################
# Security Address (Address Book)
################################################################################

class SecurityAddressView(generic.ObjectView):
    queryset = SecurityAddress.objects.all()
    table = SecurityAddressTable


class SecurityAddressListView(generic.ObjectListView):
    queryset = SecurityAddress.objects.all()
    filterset = SecurityAddressFilterSet
    filterset_form = SecurityAddressFilterForm
    table = SecurityAddressTable


class SecurityAddressEditView(generic.ObjectEditView):
    queryset = SecurityAddress.objects.all()
    form = SecurityAddressForm


class SecurityAddressBulkEditView(generic.BulkEditView):
    queryset = SecurityAddress.objects.all()
    filterset = SecurityAddressFilterSet
    table = SecurityAddressTable
    form = SecurityAddressBulkEditForm


class SecurityAddressDeleteView(generic.ObjectDeleteView):
    queryset = SecurityAddress.objects.all()
    default_return_url = 'plugins:netbox_juniper:securityaddress_list'


class SecurityAddressBulkDeleteView(generic.BulkDeleteView):
    queryset = SecurityAddress.objects.all()
    table = SecurityAddressTable


class SecurityAddressBulkImportView(generic.BulkImportView):
    queryset = SecurityAddress.objects.all()
    model_form = SecurityAddressImportForm


################################################################################
# Security Address Set (Address Book)
################################################################################

class SecurityAddressSetView(generic.ObjectView):
    queryset = SecurityAddressSet.objects.all()
    table = SecurityAddressSetTable


class SecurityAddressSetListView(generic.ObjectListView):
    queryset = SecurityAddressSet.objects.all()
    filterset = SecurityAddressSetFilterSet
    filterset_form = SecurityAddressSetFilterForm
    table = SecurityAddressSetTable


class SecurityAddressSetEditView(generic.ObjectEditView):
    queryset = SecurityAddressSet.objects.all()
    form = SecurityAddressSetForm


class SecurityAddressSetBulkEditView(generic.BulkEditView):
    queryset = SecurityAddressSet.objects.all()
    filterset = SecurityAddressSetFilterSet
    table = SecurityAddressSetTable
    form = SecurityAddressSetBulkEditForm


class SecurityAddressSetDeleteView(generic.ObjectDeleteView):
    queryset = SecurityAddressSet.objects.all()
    default_return_url = 'plugins:netbox_juniper:securityaddressset_list'


class SecurityAddressSetBulkDeleteView(generic.BulkDeleteView):
    queryset = SecurityAddressSet.objects.all()
    table = SecurityAddressSetTable


class SecurityAddressSetBulkImportView(generic.BulkImportView):
    queryset = SecurityAddressSet.objects.all()
    model_form = SecurityAddressSetImportForm
