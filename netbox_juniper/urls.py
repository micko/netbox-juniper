from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from netbox_juniper.models import *
from netbox_juniper.views import *


urlpatterns = (

    # Security Address
    path('security-address/', SecurityAddressListView.as_view(), name='securityaddress_list'),
    path('security-address/add/', SecurityAddressEditView.as_view(), name='securityaddress_add'),
    path('security-address/import/', SecurityAddressBulkImportView.as_view(), name='securityaddress_import'),
    path('security-address/edit/', SecurityAddressBulkEditView.as_view(), name='securityaddress_bulk_edit'),
    path('security-address/<int:pk>/', SecurityAddressView.as_view(), name='securityaddress'),
    path('security-address/<int:pk>/edit/', SecurityAddressEditView.as_view(), name='securityaddress_edit'),
    path('security-address/<int:pk>/delete/', SecurityAddressDeleteView.as_view(), name='securityaddress_delete'),
    path('security-address/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='securityaddress_changelog', kwargs={
        'model': SecurityAddress
    }),

    # Security Address Set
    path('security-address-set/', SecurityAddressSetListView.as_view(), name='securityaddressset_list'),
    path('security-address-set/add/', SecurityAddressSetEditView.as_view(), name='securityaddressset_add'),
    path('security-address-set/import/', SecurityAddressSetBulkImportView.as_view(), name='securityaddressset_import'),
    path('security-address-set/edit/', SecurityAddressSetBulkEditView.as_view(), name='securityaddressset_bulk_edit'),
    path('security-address-set/<int:pk>/', SecurityAddressSetView.as_view(), name='securityaddressset'),
    path('security-address-set/<int:pk>/edit/', SecurityAddressSetEditView.as_view(), name='securityaddressset_edit'),
    path('security-address-set/<int:pk>/delete/', SecurityAddressSetDeleteView.as_view(), name='securityaddressset_delete'),
    path('security-address-set/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='securityaddressset_changelog', kwargs={
        'model': SecurityAddressSet
    }),

    # Security Zone
    path('security-zone/', SecurityZoneListView.as_view(), name='securityzone_list'),
    path('security-zone/add/', SecurityZoneEditView.as_view(), name='securityzone_add'),
    path('security-zone/import/', SecurityZoneBulkImportView.as_view(), name='securityzone_import'),
    path('security-zone/edit/', SecurityZoneBulkEditView.as_view(), name='securityzone_bulk_edit'),
    path('security-zone/<int:pk>/', SecurityZoneView.as_view(), name='securityzone'),
    path('security-zone/<int:pk>/edit/', SecurityZoneEditView.as_view(), name='securityzone_edit'),
    path('security-zone/<int:pk>/delete/', SecurityZoneDeleteView.as_view(), name='securityzone_delete'),
    path('security-zone/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='securityzone_changelog', kwargs={
        'model': SecurityZone
    }),

)
