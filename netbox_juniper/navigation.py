from django.utils.translation import gettext_lazy as _
from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu

################################################################################
# Applications
################################################################################

application_item = PluginMenuItem(
    link="plugins:netbox_juniper:application_list",
    link_text=_("Applications"),
    buttons=(
        PluginMenuButton(
            'plugins:netbox_juniper:application_add',
            _("Add"),
            'mdi mdi-plus-thick',
        ),
        PluginMenuButton(
            link='plugins:netbox_juniper:application_import',
            title='Import',
            icon_class='mdi mdi-upload',
        ),
    ),
)

application_set_item = PluginMenuItem(
    link="plugins:netbox_juniper:applicationset_list",
    link_text=_("Application Sets"),
    buttons=(
        PluginMenuButton(
            'plugins:netbox_juniper:applicationset_add',
            _("Add"),
            'mdi mdi-plus-thick',
        ),
        PluginMenuButton(
            link='plugins:netbox_juniper:applicationset_import',
            title='Import',
            icon_class='mdi mdi-upload',
        ),
    ),
)

################################################################################
# Security
################################################################################

security_address_item = PluginMenuItem(
    link="plugins:netbox_juniper:securityaddress_list",
    link_text=_("Addresses"),
    buttons=(
        PluginMenuButton(
            'plugins:netbox_juniper:securityaddress_add',
            _("Add"),
            'mdi mdi-plus-thick',
        ),
        PluginMenuButton(
            link='plugins:netbox_juniper:securityaddress_import',
            title='Import',
            icon_class='mdi mdi-upload',
        ),
    ),
)

security_address_set_item = PluginMenuItem(
    link="plugins:netbox_juniper:securityaddressset_list",
    link_text=_("Address Sets"),
    buttons=(
        PluginMenuButton(
            'plugins:netbox_juniper:securityaddressset_add',
            _("Add"),
            'mdi mdi-plus-thick',
        ),
        PluginMenuButton(
            link='plugins:netbox_juniper:securityaddressset_import',
            title='Import',
            icon_class='mdi mdi-upload',
        ),
    ),
)

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

################################################################################
# Menu
################################################################################

menu = PluginMenu(
    label='Juniper Networks',
    groups=(
        (
            _("Applications"),
            (
                application_item,
                application_set_item,
            ),
        ),
        (
            _("Security"),
            (
                security_address_item,
                security_address_set_item,
                security_zone_item,
            ),
        ),
    ),
    icon_class='mdi mdi-alpha-j-box',
)
