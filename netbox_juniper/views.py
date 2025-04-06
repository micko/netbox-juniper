from netbox.views import generic
from django.db.models import Count
from . import filtersets, forms, models, tables


class FirewallFilterView(generic.ObjectView):
    queryset = models.FirewallFilter.objects.all()


class FirewallFilterListView(generic.ObjectListView):
    queryset = models.FirewallFilter.objects.all()
    table = tables.FirewallFilterTable
    filterset = filtersets.FirewallFilterFilterSet
    filterset_form = forms.FirewallFilterFilterForm


class FirewallFilterEditView(generic.ObjectEditView):
    queryset = models.FirewallFilter.objects.all()
    form = forms.FirewallFilterForm


class FirewallFilterDeleteView(generic.ObjectDeleteView):
    queryset = models.FirewallFilter.objects.all()
