# Generated by Django 4.2 on 2023-04-13 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medb', '0004_alter_taken_time_taken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taken',
            old_name='time_taken',
            new_name='taken_date',
        ),
    ]
