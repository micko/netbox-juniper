from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views


urlpatterns = (
    path('firewall-filter/', views.FirewallFilterListView.as_view(), name='firewallfilter_list'),
    path('firewall-filter/add/', views.FirewallFilterEditView.as_view(), name='firewallfilter_add'),
    path('firewall-filter/<int:pk>/', views.FirewallFilterView.as_view(), name='firewallfilter'),
    path('firewall-filter/<int:pk>/edit/', views.FirewallFilterEditView.as_view(), name='firewallfilter_edit'),
    path('firewall-filter/<int:pk>/delete/', views.FirewallFilterDeleteView.as_view(), name='firewallfilter_delete'),
    path('firewall-filter/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='firewallfilter_changelog', kwargs={
        'model': models.FirewallFilter
    }),
)
