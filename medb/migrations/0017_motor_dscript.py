# Generated by Django 4.2 on 2023-04-20 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medb', '0016_pills_motor_delete_motor_pill'),
    ]

    operations = [
        migrations.AddField(
            model_name='motor',
            name='dscript',
            field=models.SlugField(default='/somepath'),
        ),
    ]
