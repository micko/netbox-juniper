from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'netbox_juniper'


router = NetBoxRouter()
router.register('firewall-filter', views.FirewallFilterViewSet)
router.register('firewall-policer', views.FirewallPolicerViewSet)

# security
router.register('security-zone', views.SecurityZoneViewSet)

urlpatterns = router.urls
