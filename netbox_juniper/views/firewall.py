from netbox.views import generic
from django.db.models import Count

from netbox_juniper.filtersets.firewall import *
from netbox_juniper.forms.firewall import *
from netbox_juniper.models.firewall import *
from netbox_juniper.tables.firewall import *

#
# Firewall Filter
#

class FirewallFilterView(generic.ObjectView):
    queryset = FirewallFilter.objects.all()
    table = FirewallFilterTable


class FirewallFilterListView(generic.ObjectListView):
    queryset = FirewallFilter.objects.all()
    filterset = FirewallFilterFilterSet
    filterset_form = FirewallFilterFilterForm
    table = FirewallFilterTable


class FirewallFilterEditView(generic.ObjectEditView):
    queryset = FirewallFilter.objects.all()
    form = FirewallFilterForm


class FirewallFilterBulkEditView(generic.BulkEditView):
    queryset = FirewallFilter.objects.all()
    filterset = FirewallFilterFilterSet
    table = FirewallFilterTable
    form = FirewallFilterBulkEditForm


class FirewallFilterDeleteView(generic.ObjectDeleteView):
    queryset = FirewallFilter.objects.all()
    default_return_url = 'plugins:netbox_juniper:firewallfilter_list'


class FirewallFilterBulkDeleteView(generic.BulkDeleteView):
    queryset = FirewallFilter.objects.all()
    table = FirewallFilterTable


class FirewallFilterBulkImportView(generic.BulkImportView):
    queryset = FirewallFilter.objects.all()
    model_form = FirewallFilterImportForm


#
# Firewall Policer
#

class FirewallPolicerView(generic.ObjectView):
    queryset = FirewallPolicer.objects.all()
    table = FirewallPolicerTable


class FirewallPolicerListView(generic.ObjectListView):
    queryset = FirewallPolicer.objects.all()
    filterset = FirewallPolicerFilterSet
    filterset_form = FirewallPolicerFilterForm
    table = FirewallPolicerTable


class FirewallPolicerEditView(generic.ObjectEditView):
    queryset = FirewallPolicer.objects.all()
    form = FirewallPolicerForm


class FirewallPolicerBulkEditView(generic.BulkEditView):
    queryset = FirewallPolicer.objects.all()
    filterset = FirewallPolicerFilterSet
    table = FirewallPolicerTable
    form = FirewallPolicerBulkEditForm


class FirewallPolicerDeleteView(generic.ObjectDeleteView):
    queryset = FirewallPolicer.objects.all()
    default_return_url = 'plugins:netbox_juniper:firewallpolicer_list'


class FirewallPolicerBulkDeleteView(generic.BulkDeleteView):
    queryset = FirewallPolicer.objects.all()
    table = FirewallPolicerTable


class FirewallPolicerBulkImportView(generic.BulkImportView):
    queryset = FirewallPolicer.objects.all()
    model_form = FirewallPolicerImportForm
