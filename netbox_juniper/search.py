from netbox.search import SearchIndex, register_search
from . models import FirewallFilter


@register_search
class FirewallFilterIndex(SearchIndex):
    model = FirewallFilter
    fields = (
        ('name', 100),
        ('device', 200),
    )
