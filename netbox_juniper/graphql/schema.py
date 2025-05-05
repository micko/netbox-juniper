from typing import List

import strawberry
import strawberry_django

from netbox_juniper.models import *

from . types import *

@strawberry.type(name="Query")
class SecurityQuery:
    security_address: SecurityAddressType = strawberry_django.field()
    security_address_list: List[SecurityAddressType] = strawberry_django.field()

    security_address_set: SecurityAddressSetType = strawberry_django.field()
    security_address_set_list: List[SecurityAddressSetType] = strawberry_django.field()

    security_zone: SecurityZoneType = strawberry_django.field()
    security_zone_list: List[SecurityZoneType] = strawberry_django.field()

