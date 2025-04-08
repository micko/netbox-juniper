from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from netbox_juniper.models import *
from netbox_juniper.views import *


urlpatterns = (

    # Firewall Filter
    path('firewall-filter/', FirewallFilterListView.as_view(), name='firewallfilter_list'),
    path('firewall-filter/add/', FirewallFilterEditView.as_view(), name='firewallfilter_add'),
    path('firewall-filter/import/', FirewallFilterBulkImportView.as_view(), name='firewallfilter_import'),
    path('firewall-filter/edit/', FirewallFilterBulkEditView.as_view(), name='firewallfilter_bulk_edit'),
    path('firewall-filter/<int:pk>/', FirewallFilterView.as_view(), name='firewallfilter'),
    path('firewall-filter/<int:pk>/edit/', FirewallFilterEditView.as_view(), name='firewallfilter_edit'),
    path('firewall-filter/<int:pk>/delete/', FirewallFilterDeleteView.as_view(), name='firewallfilter_delete'),
    path('firewall-filter/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='firewallfilter_changelog', kwargs={
        'model': FirewallFilter
    }),

    # Firewall Policer
    path('firewall-policer/', FirewallPolicerListView.as_view(), name='firewallpolicer_list'),
    path('firewall-policer/add/', FirewallPolicerEditView.as_view(), name='firewallpolicer_add'),
    path('firewall-policer/import/', FirewallPolicerBulkImportView.as_view(), name='firewallpolicer_import'),
    path('firewall-policer/edit/', FirewallPolicerBulkEditView.as_view(), name='firewallpolicer_bulk_edit'),
    path('firewall-policer/<int:pk>/', FirewallPolicerView.as_view(), name='firewallpolicer'),
    path('firewall-policer/<int:pk>/edit/', FirewallPolicerEditView.as_view(), name='firewallpolicer_edit'),
    path('firewall-policer/<int:pk>/delete/', FirewallPolicerDeleteView.as_view(), name='firewallpolicer_delete'),
    path('firewall-policer/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='firewallpolicer_changelog', kwargs={
        'model': FirewallPolicer
    }),

)
