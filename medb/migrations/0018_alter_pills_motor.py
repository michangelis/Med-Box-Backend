# Generated by Django 5.1.3 on 2024-11-19 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medb', '0017_motor_dscript'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pills',
            name='motor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medb.motor'),
        ),
    ]