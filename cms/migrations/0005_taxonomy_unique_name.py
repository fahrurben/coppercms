# Generated by Django 5.0.2 on 2024-02-13 15:13

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_taxonomy'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='taxonomy',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), models.F('group'), name='unique_name'),
        ),
    ]
