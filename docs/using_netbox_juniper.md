# Supported features

## Applications

`application` and `application-set` provide you with the capability to define various application definitions that you can use to reference in a `security-policy`. These can be configured either `global` (meaning for your entire network deployment) or per `device`.

## Security

### Address Book

`security-address` and `security-address-set` are part of the Address Book feature that you can use reference with a `security-policy` which JunOS requires for address matching. These can configured either `global` (meaning it can be used across multiple security zones) or per `security-zone`.

### Security Zone

`security-zone` is a logical definition that segments your network based various rules for inbound and outbound traffic. In order for any security zone to be active an `interface` has to be selected (address) to the zone.
