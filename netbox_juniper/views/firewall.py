from netbox.views import generic
from django.db.models import Count

#from netbox_juniper.filtersets import *
from netbox_juniper.forms import *
from netbox_juniper.models import *
from netbox_juniper.tables import *


class FirewallFilterView(generic.ObjectView):
    queryset = FirewallFilter.objects.all()


class FirewallFilterListView(generic.ObjectListView):
    queryset = FirewallFilter.objects.all()
    table = FirewallFilterTable


class FirewallFilterEditView(generic.ObjectEditView):
    queryset = FirewallFilter.objects.all()
    form = FirewallFilterForm


class FirewallFilterDeleteView(generic.ObjectDeleteView):
    queryset = FirewallFilter.objects.all()
