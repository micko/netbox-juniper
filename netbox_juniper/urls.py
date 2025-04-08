from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from netbox_juniper.models import *
from netbox_juniper.views import *


urlpatterns = (

    # Firewall Filter
    path('firewall-filter/', FirewallFilterListView.as_view(), name='firewallfilter_list'),
    path('firewall-filter/add/', FirewallFilterEditView.as_view(), name='firewallfilter_add'),
    path('firewall-filter/<int:pk>/', FirewallFilterView.as_view(), name='firewallfilter'),
    path('firewall-filter/<int:pk>/edit/', FirewallFilterEditView.as_view(), name='firewallfilter_edit'),
    path('firewall-filter/<int:pk>/delete/', FirewallFilterDeleteView.as_view(), name='firewallfilter_delete'),
    path('firewall-filter/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='firewallfilter_changelog', kwargs={
        'model': FirewallFilter
    }),

)
