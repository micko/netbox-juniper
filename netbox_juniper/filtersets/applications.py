import django_filters
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from django.utils.translation import gettext as _

from utilities.filters import (
    ContentTypeFilter,
    MultiValueCharFilter,
    MultiValueNumberFilter,
    NumericArrayFilter,
    TreeNodeMultipleChoiceFilter,
)

from netbox_juniper.models.applications import *

################################################################################
# Application
################################################################################

class ApplicationFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Application
        fields = ('id', 'name', 'device', 'description', 'comments')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(device__icontains=value)
            | Q(description__icontains=value)
            | Q(comments__icontains=value)
        )
        return queryset.filter(qs_filter)

################################################################################
# Application Set
################################################################################

class ApplicationSetFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = ApplicationSet
        fields = ('id', 'name', 'device', 'application', 'description', 'comments')

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value)
            | Q(device__icontains=value)
            | Q(application_icontains=value)
            | Q(description__icontains=value)
            | Q(comments__icontains=value)
        )
        return queryset.filter(qs_filter)
