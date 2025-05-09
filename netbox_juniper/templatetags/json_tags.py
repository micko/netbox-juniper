import json
from django import template
from django.db.models import Model

register = template.Library()

@register.filter(name='to_json')
def to_json(instance):
    if not isinstance(instance, Model):
        return json.dumps(str(instance))  # fallback for non-models

    data = {}
    for field in instance._meta.get_fields():
        if hasattr(field, 'attname'):  # skip reverse and many-to-many fields
            try:
                value = getattr(instance, field.attname)
                data[field.name] = value
            except Exception:
                data[field.name] = '<<error>>'

    return json.dumps(data, indent=2, default=str)
