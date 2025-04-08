from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'netbox_juniper'


router = NetBoxRouter()
router.register('firewall-filter', views.FirewallFilterViewSet)

urlpatterns = router.urls
