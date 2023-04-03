# Generated by Django 4.1.7 on 2023-04-03 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('weight', models.DecimalField(decimal_places=3, max_digits=3)),
                ('company', models.CharField(max_length=255)),
                ('inventory', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.IntegerField(max_length=10)),
                ('desc', models.TextField(null=True)),
                ('pills', models.ManyToManyField(to='box.pill')),
            ],
        ),
        migrations.CreateModel(
            name='PerPill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pill_intake', models.TimeField()),
                ('dose', models.IntegerField()),
                ('pill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='box.pill')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken', models.BooleanField()),
                ('pill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='box.pill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='box.user')),
            ],
        ),
    ]
