# Generated by Django 5.2 on 2025-05-08 00:01

import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0207_remove_redundant_indexes'),
        ('extras', '0128_tableconfig'),
        ('netbox_juniper', '0003_securityaddressset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=64)),
                ('is_global', models.BooleanField(default=False)),
                ('application_protocol', models.CharField(blank=True, max_length=128)),
                ('inactivity_timeout', models.CharField(blank=True, max_length=64)),
                ('protocol', models.CharField(blank=True, max_length=64)),
                ('source_port', models.CharField(blank=True, max_length=64)),
                ('destination_port', models.CharField(blank=True, max_length=64)),
                ('icmp_code', models.CharField(blank=True, max_length=64)),
                ('icmp_type', models.CharField(blank=True, max_length=64)),
                ('icmp6_code', models.CharField(blank=True, max_length=64)),
                ('icmp6_type', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('comments', models.TextField(blank=True)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
                'ordering': ['name', 'is_global', 'device'],
            },
        ),
        migrations.CreateModel(
            name='ApplicationSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=64)),
                ('is_global', models.BooleanField(default=False)),
                ('application', models.ManyToManyField(to='netbox_juniper.application')),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'Application Set',
                'verbose_name_plural': 'Application Sets',
                'ordering': ['name', 'is_global', 'device'],
            },
        ),
        migrations.AddIndex(
            model_name='application',
            index=models.Index(fields=['name'], name='idx_application_name'),
        ),
        migrations.AddConstraint(
            model_name='application',
            constraint=models.CheckConstraint(condition=models.Q(models.Q(('device', True), ('is_global', True)), models.Q(('device__isnull', False), ('is_global', False)), _connector='OR'), name='unique_application_configured'),
        ),
        migrations.AddConstraint(
            model_name='application',
            constraint=models.UniqueConstraint(fields=('name', 'device'), name='unique_application_name'),
        ),
        migrations.AddIndex(
            model_name='applicationset',
            index=models.Index(fields=['name'], name='idx_application_set_name'),
        ),
        migrations.AddConstraint(
            model_name='applicationset',
            constraint=models.CheckConstraint(condition=models.Q(models.Q(('device', True), ('is_global', True)), models.Q(('device__isnull', False), ('is_global', False)), _connector='OR'), name='unique_application_set_configured'),
        ),
        migrations.AddConstraint(
            model_name='applicationset',
            constraint=models.UniqueConstraint(fields=('name', 'device'), name='unique_application_set_name'),
        ),
    ]
