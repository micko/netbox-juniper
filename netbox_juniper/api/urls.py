from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_juniper'

router = NetBoxRouter()

################################################################################
# Security
################################################################################

router.register('security-address', views.SecurityAddressViewSet)
router.register('security-address-set', views.SecurityAddressSetViewSet)
router.register('security-zone', views.SecurityZoneViewSet)

urlpatterns = router.urls

