from netbox.plugins import PluginConfig


class JuniperConfig(PluginConfig):
    name = 'netbox_juniper'
    verbose_name = 'Juniper Networks'
    description = 'Juniper Networks Plugin for NetBox'
    version = '0.1'
    author = 'Dragan Mickovic'
    author_email = 'dmickovic@gmail.com'
    base_url = 'juniper'


config = JuniperConfig
