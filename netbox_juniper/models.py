from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel

class FirewallFilter(NetBoxModel):
    name = models.CharField(max_length=64, unique=True)
    family = models.CharField(max_length=20, choices=[('inet', 'IPv4'), ('inet6', 'IPv6'), ('ethernet-switching', 'Layer 2')])
    description = models.CharField(max_length=200, blank=True)
    device = models.ForeignKey('dcim.Device', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['device', 'name'], name='unique_firewall_filter')
        ]

    def get_absolute_url(self):
        return reverse('plugins:netbox_juniper:firewallfilter', args=[self.pk])

#class FilterTerm(models.Model):
#    filter = models.ForeignKey(FirewallFilter, on_delete=models.CASCADE, related_name='terms')
#    name = models.CharField(max_length=64)
#    protocol = models.CharField(max_length=20, blank=True)
#
#    class Meta:
#        unique_together = ('filter', 'name')
