from netbox.views import generic
from django.db.models import Count

from netbox_juniper.filtersets.applications import *
from netbox_juniper.forms import *
from netbox_juniper.models.applications import *
from netbox_juniper.tables.applications import *

################################################################################
# Application
################################################################################

class ApplicationView(generic.ObjectView):
    queryset = Application.objects.all()
    table = ApplicationTable


class ApplicationListView(generic.ObjectListView):
    queryset = Application.objects.all()
    filterset = ApplicationFilterSet
    filterset_form = ApplicationFilterForm
    table = ApplicationTable


class ApplicationEditView(generic.ObjectEditView):
    queryset = Application.objects.all()
    form = ApplicationForm


class ApplicationBulkEditView(generic.BulkEditView):
    queryset = Application.objects.all()
    filterset = ApplicationFilterSet
    table = ApplicationTable
    form = ApplicationBulkEditForm


class ApplicationDeleteView(generic.ObjectDeleteView):
    queryset = Application.objects.all()
    default_return_url = 'plugins:netbox_juniper:application_list'


class ApplicationBulkDeleteView(generic.BulkDeleteView):
    queryset = Application.objects.all()
    table = ApplicationTable


class ApplicationBulkImportView(generic.BulkImportView):
    queryset = Application.objects.all()
    model_form = ApplicationImportForm


################################################################################
# Application Set
################################################################################

class ApplicationSetView(generic.ObjectView):
    queryset = ApplicationSet.objects.all()
    table = ApplicationSetTable


class ApplicationSetListView(generic.ObjectListView):
    queryset = ApplicationSet.objects.all()
    filterset = ApplicationSetFilterSet
    filterset_form = ApplicationSetFilterForm
    table = ApplicationSetTable


class ApplicationSetEditView(generic.ObjectEditView):
    queryset = ApplicationSet.objects.all()
    form = ApplicationSetForm


class ApplicationSetBulkEditView(generic.BulkEditView):
    queryset = ApplicationSet.objects.all()
    filterset = ApplicationSetFilterSet
    table = ApplicationSetTable
    form = ApplicationSetBulkEditForm


class ApplicationSetDeleteView(generic.ObjectDeleteView):
    queryset = ApplicationSet.objects.all()
    default_return_url = 'plugins:netbox_juniper:applicationset_list'


class ApplicationSetBulkDeleteView(generic.BulkDeleteView):
    queryset = ApplicationSet.objects.all()
    table = ApplicationSetTable


class ApplicationSetBulkImportView(generic.BulkImportView):
    queryset = ApplicationSet.objects.all()
    model_form = ApplicationSetImportForm
