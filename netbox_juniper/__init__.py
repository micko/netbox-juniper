from netbox.plugins import PluginConfig
from .version import __version__


class JuniperConfig(PluginConfig):
    name = 'netbox_juniper'
    verbose_name = 'Juniper Networks'
    description = 'Juniper Networks Plugin for NetBox'
    version = __version__
    author = 'Dragan Mickovic'
    author_email = 'dmickovic@gmail.com'
    base_url = 'juniper'
    required_settings = []
    default_settings = {
        'top_level_menu' : True,
    }


config = JuniperConfig
