# Generated by Django 3.2.6 on 2021-08-16 03:53

import buku.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='tahun',
            field=models.PositiveIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1900), buku.models.max_value_current_year]),
        ),
    ]
