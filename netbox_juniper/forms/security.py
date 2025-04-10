from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.forms import SimpleArrayField
from utilities.forms.fields import (
    DynamicModelChoiceField,
    CSVModelChoiceField,
    CSVModelMultipleChoiceField,
    DynamicModelMultipleChoiceField,
    TagFilterField,
    CSVChoiceField,
    CommentField,
)
from utilities.forms.rendering import FieldSet
from dcim.models import Device, Interface
from netbox.forms import (
    NetBoxModelForm,
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
)

from netbox_juniper.models.security import *

#
# Security Zone
#

class SecurityZoneForm(NetBoxModelForm):
    device = DynamicModelChoiceField(
        label=_('Device'),
        queryset=Device.objects.all(),
        required=True,
    )
    interfaces = DynamicModelMultipleChoiceField(
        label=_('Interfaces'),
        queryset=Interface.objects.all(),
        required=False,
        query_params={
            'device_id': '$device',
        }
    )
    host_inbound_traffic_protocols = forms.MultipleChoiceField(
        choices=SecurityZoneHostInboundTrafficProtocolsChoices,
        label=_('Protocols'),
        widget=forms.SelectMultiple,
        required=False,
        help_text=_('Protocol type of incoming traffic to accept')
    )
    host_inbound_traffic_services = forms.MultipleChoiceField( 
        choices=SecurityZoneHostInboundTrafficServicesChoices,
        label=_('Services'),
        widget=forms.SelectMultiple,
        required=False,
        help_text=_('Type of incoming system-service traffic to accept')
    )

    comments = CommentField()

#    fieldsets = (
#        FieldSet(
#            'name', 'device', 'interfaces', 'description', name=_('Zone Info')
#        ),
#        FieldSet(
#            'proto_all', 'proto_bfd', 'proto_bgp', 'proto_dvmrp', 'proto_igmp', 'proto_ldp', 'proto_msdp',
#            'proto_nhrp', 'proto_ospf', 'proto_ospf3', 'proto_pgm', 'proto_pim', 'proto_rip', 'proto_ripng',
#            'proto_router_discovery', 'proto_rsvp', 'proto_sap', 'proto_vrrp', name=_('Protocol type of incoming traffic to accept')
#        ),
#        FieldSet(
#            'service_all', 'service_any_service', 'service_appqoe', 'service_bootp', 'service_dhcp', 'service_dhcpv6',
#            'service_dns', 'service_finger', 'service_ftp', 'service_high_availability', 'service_http', 'service_https',
#            'service_ident_reset', 'service_ike', 'service_lsping', 'service_lsselfping', 'service_netconf', 'service_ntp',
#            'service_ping', 'service_r2cp', 'service_reverse_ssh', 'service_reverse_telnet', 'service_rlogin', 'service_rpm',
#            'service_rsh', 'service_snmp', 'service_snmp_trap', 'service_ssh', 'service_tcp_encap', 'service_telnet',
#            'service_tftp', 'service_traceroute', 'service_webapi_clear_text', 'service_webapi_ssl', 'service_xnm_clear_text',
#            'service_xnm_ssl', name=_('Type of incoming system-service traffic to accept')
#        ),
#        FieldSet(
#            'application_tracking', 'enable_reverse_reroute', 'tcp_rst', 'unidirectional_session_refreshing',
#            name=_('Miscellaneous')
#        ),
#    )

    class Meta:
        model = SecurityZone
        fields = (
            'name', 'device', 'interfaces', 'host_inbound_traffic_protocols', 'host_inbound_traffic_services',
            'application_tracking', 'enable_reverse_reroute', 'tcp_rst', 'unidirectional_session_refreshing',
            'description', 'comments', 'tags'
        )


class SecurityZoneFilterForm(NetBoxModelFilterSetForm):
    model = SecurityZone

    q = forms.CharField(required=False, label="Search")

    name = forms.CharField(max_length=64, required=False)

    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )

    tag = TagFilterField(SecurityZone)


class SecurityZoneBulkEditForm(NetBoxModelBulkEditForm):
    model = SecurityZone

    name = forms.CharField(max_length=64, required=False)
    device = DynamicModelChoiceField(
        label=_("Device"),
        queryset=Device.objects.all(),
        required=True,
    )
    interfaces = DynamicModelMultipleChoiceField(
        label=_("Interfaces"),
        queryset=Interface.objects.all(),
        required=False,
    )

    application_tracking = forms.BooleanField(
        required=False,
    )
    enable_reverse_reroute = forms.BooleanField(
        required=False,
    )
    tcp_rst = forms.BooleanField(
        required=False,
    )
    unidirectional_session_refreshing = forms.BooleanField(
        required=False,
    )
    # remaining
    description = forms.CharField(
        required=False,
    )
    comments = CommentField()


class SecurityZoneImportForm(NetBoxModelImportForm):
    device = CSVModelChoiceField(
        label=_('Device'),
        queryset=Device.objects.all(),
        required=True,
        to_field_name="device",
        help_text=_("Device"),
    )
    interfaces = CSVModelMultipleChoiceField(
        label=_('Interfaces'),
        queryset=Interface.objects.all(),
        required=False,
        to_field_name="interfaces",
        help_text=_("Interfaces"),
    )


    class Meta:
        model = SecurityZone
        fields = (
            'name', 'device', 'interfaces', 'host_inbound_traffic_protocols', 'host_inbound_traffic_services',
            'application_tracking', 'enable_reverse_reroute', 'tcp_rst', 'unidirectional_session_refreshing',
            'description', 'comments', 'tags'
        )
