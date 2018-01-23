# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerServiceMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Must be unique.', unique=True, verbose_name='Unique Identifier')),
                ('message', models.CharField(blank=True, default='', help_text='Message details.', max_length=256, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]