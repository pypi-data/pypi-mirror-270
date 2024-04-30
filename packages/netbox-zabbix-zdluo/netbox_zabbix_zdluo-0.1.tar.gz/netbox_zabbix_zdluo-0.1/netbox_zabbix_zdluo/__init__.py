from extras.plugins import PluginConfig

class ZabbixPluginConfig(PluginConfig):
    name = 'netbox_zabbix_zdluo'
    verbose_name = 'NetBox Zabbix Plugin'
    version = '0.1'
    author = 'Your Name'
    description = 'A plugin for NetBox.'
#    base_url = 'netbox-zabbix-plugin'

config = ZabbixPluginConfig