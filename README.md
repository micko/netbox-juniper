# NetBox Juniper
[Netbox](https://github.com/netbox-community/netbox) plugin for [Juniper Networks](https://www.juniper.net) device configuration components.

<div align="center">
<a href="https://pypi.org/project/netbox-juniper/"><img src="https://img.shields.io/pypi/v/netbox-juniper" alt="PyPi"/></a>
<a href="https://github.com/micko/netbox-juniper/stargazers"><img src="https://img.shields.io/github/stars/micko/netbox-juniper?style=flat" alt="Stars Badge"/></a>
<a href="https://github.com/micko/netbox-juniper/network/members"><img src="https://img.shields.io/github/forks/micko/netbox-juniper?style=flat" alt="Forks Badge"/></a>
<a href="https://github.com/micko/netbox-juniper/issues"><img src="https://img.shields.io/github/issues/micko/netbox-juniper" alt="Issues Badge"/></a>
<a href="https://github.com/micko/netbox-juniper/pulls"><img src="https://img.shields.io/github/issues-pr/micko/netbox-juniper" alt="Pull Requests Badge"/></a>
<a href="https://github.com/micko/netbox-juniper/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/micko/netbox-juniper?color=2b9348"></a>
<a href="https://github.com/micko/netbox-juniper/blob/master/LICENSE"><img src="https://img.shields.io/github/license/micko/netbox-juniper?color=2b9348" alt="License Badge"/></a>
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style Black"/></a>
</div>

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
