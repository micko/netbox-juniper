from netbox.plugins.utils import get_plugin_config
from django.utils.translation import gettext_lazy as _
from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu


firewall_filter_item = PluginMenuItem(
    link="plugins:netbox_juniper:firewallfilter_list",
    link_text=_("Filters"),
    buttons=(
        PluginMenuButton(
            'plugins:netbox_juniper:firewallfilter_add',
            _("Add"),
            'mdi mdi-plus-thick',
        ),
#        PluginMenuButton(
#            'plugins:netbox_juniper:firewallfilter_import',
#            _("Import"),
#            'mdi mdi-upload',
#        ),
    ),
)

menu = PluginMenu(
    label='Juniper Networks',
    groups=(
        (
            _("Firewall"),
            (
                firewall_filter_item,
            ),
        ),
    ),
    icon_class='mdi mdi-alpha-j-box',
)
