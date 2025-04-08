# Generated by Django 5.1.7 on 2025-04-08 00:33

import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0200_populate_mac_addresses'),
        ('extras', '0123_journalentry_kind_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirewallFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=64)),
                ('family', models.CharField(max_length=20)),
                ('comments', models.TextField(blank=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'Firewall Filter',
                'verbose_name_plural': 'Firewall Filters',
                'ordering': ['device', 'name'],
                'indexes': [models.Index(fields=['name'], name='idx_firewall_filter_name')],
                'constraints': [models.UniqueConstraint(fields=('device', 'name'), name='unique_firewall_filter')],
            },
        ),
    ]
