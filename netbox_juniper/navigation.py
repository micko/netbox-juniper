from django.utils.translation import gettext_lazy as _
from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu

#
# Firewall
#

firewall_filter_item = PluginMenuItem(
    link="plugins:netbox_juniper:firewallfilter_list",
    link_text=_("Filters"),
    buttons=(
        PluginMenuButton(
            'plugins:netbox_juniper:firewallfilter_add',
            _("Add"),
            'mdi mdi-plus-thick',
        ),
        PluginMenuButton(
            link='plugins:netbox_juniper:firewallfilter_import',
            title='Import',
            icon_class='mdi mdi-upload',
        ),      
    ),
)

firewall_policer_item = PluginMenuItem(
    link="plugins:netbox_juniper:firewallpolicer_list",
    link_text=_("Policers"),
    buttons=(
        PluginMenuButton(
            'plugins:netbox_juniper:firewallpolicer_add',
            _("Add"),
            'mdi mdi-plus-thick',
        ),
        PluginMenuButton(
            link='plugins:netbox_juniper:firewallpolicer_import',
            title='Import',
            icon_class='mdi mdi-upload',
        ),
    ),
)

# 
# Security
#

security_zone_item = PluginMenuItem(
    link="plugins:netbox_juniper:securityzone_list",
    link_text=_("Zones"),
    buttons=(
        PluginMenuButton(
            'plugins:netbox_juniper:securityzone_add',
            _("Add"),
            'mdi mdi-plus-thick',
        ),
        PluginMenuButton(
            link='plugins:netbox_juniper:securityzone_import',
            title='Import',
            icon_class='mdi mdi-upload',
        ),
    ),
)

security_addressbook_addrss_item = PluginMenuItem(
    link="plugins:netbox_juniper:addressbookaddress",
    link_text=_("Addresses"),
    buttons=(
        PluginMenuButton(
            'plugins:netbox_juniper:addressbookaddress_add',
            _("Add"),
            'mdi mdi-plus-thick',
        ),
        PluginMenuButton(
            link='plugins:netbox_juniper:addressbookaddress_import',
            title='Import',
            icon_class='mdi mdi-upload',
        ),
    ),
)



menu = PluginMenu(
    label='Juniper Networks',
    groups=(
        (
            _("Firewall"),
            (
                firewall_filter_item,
                firewall_policer_item,
            ),
        ),
        (
            _("Security"),
            (
                _("Address Books"),
                (
                    security_addressbook_addrss_item
                ),
                _("Zones"),
                (
                    security_zone_item,
                )
            ),
        ),
    ),
    icon_class='mdi mdi-alpha-j-box',
)
