from netbox.views import generic
from django.db.models import Count

from utilities.permissions import get_permission_for_model

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
    permission = 'netbox_juniper.view_security'


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

#
# Address Book - Address
#

class AddressBookAddressView(generic.ObjectView):
    queryset = AddressBookAddress.objects.all()
    table = AddressBookAddressTable


class AddressBookAddressListView(generic.ObjectListView):
    queryset = AddressBookAddress.objects.all()
    filterset = AddressBookAddressFilterSet
    filterset_form = AddressBookAddressFilterForm
    table = AddressBookAddressTable
    permission = 'netbox_juniper.view_security'


class AddressBookAddressEditView(generic.ObjectEditView):
    queryset = AddressBookAddress.objects.all()
    form = AddressBookAddressForm


class AddressBookAddressBulkEditView(generic.BulkEditView):
    queryset = AddressBookAddress.objects.all()
    filterset = AddressBookAddressFilterSet
    table = AddressBookAddressTable
    form = AddressBookAddressBulkEditForm


class AddressBookAddressDeleteView(generic.ObjectDeleteView):
    queryset = AddressBookAddress.objects.all()
    default_return_url = 'plugins:netbox_juniper:addressbookaddress_list'


class AddressBookAddressBulkDeleteView(generic.BulkDeleteView):
    queryset = AddressBookAddress.objects.all()
    table = AddressBookAddressTable


class AddressBookAddressBulkImportView(generic.BulkImportView):
    queryset = AddressBookAddress.objects.all()
    model_form = AddressBookAddressImportForm

