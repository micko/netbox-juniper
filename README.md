# NetBox Juniper
[Netbox](https://github.com/netbox-community/netbox) plugin for [Juniper Networks](https://www.juniper.net) device configuration components.

## Objectives
NetBox Juniper Plugin is designed to help with the configuration of certain Juniper Networks specific configuration objects.

## WARNING
This module is Alpha at best - USE AT YOUR OWN RISK.

## Requirements
* NetBox 4.2.5 or higher
* Python 3.10 or higher

## HowTo

### Installation

```
$ source /opt/netbox/venv/bin/activate
(venv) $ pip install netbox-juniper
```

### Configuration

Add the plugin to the NetBox config: `configuration.py`

```python
PLUGINS = [
    "netbox_juniper",
]
```

Permanently keep the plugin installed `upgrade.sh`:

```
echo netbox-juniper >> local_requirements.txt
```

Run the following to get things going:

```
manage.py migrate
```

## Contribute

I am not a Python expert so if you see something that is stupid feel free to improve.

## Documentation

Coming Soon: [Using NetBox Juniper Plugin](docs/using_netbox_juniper.md)

## License

Apache 2.0
