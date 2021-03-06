# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-10 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0043_add_reservable_days_in_advance'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='reservation_info_en',
            field=models.TextField(blank=True, null=True, verbose_name='Reservation info'),
        ),
        migrations.AddField(
            model_name='resource',
            name='reservation_info_fi',
            field=models.TextField(blank=True, null=True, verbose_name='Reservation info'),
        ),
        migrations.AddField(
            model_name='resource',
            name='reservation_info_sv',
            field=models.TextField(blank=True, null=True, verbose_name='Reservation info'),
        ),
        migrations.AddField(
            model_name='resource',
            name='responsible_contact_info_en',
            field=models.TextField(blank=True, null=True, verbose_name='Responsible contact info'),
        ),
        migrations.AddField(
            model_name='resource',
            name='responsible_contact_info_fi',
            field=models.TextField(blank=True, null=True, verbose_name='Responsible contact info'),
        ),
        migrations.AddField(
            model_name='resource',
            name='responsible_contact_info_sv',
            field=models.TextField(blank=True, null=True, verbose_name='Responsible contact info'),
        ),
    ]
