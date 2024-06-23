# Generated by Django 5.0.6 on 2024-06-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_delete_networktraffic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('component', models.CharField(max_length=25)),
                ('status', models.BooleanField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('email', models.BooleanField(default=True)),
                ('sensor', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('measurement', models.CharField(max_length=25)),
                ('current_reading', models.DecimalField(decimal_places=1, max_digits=25)),
                ('status', models.CharField(default='Active', max_length=25)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_level', models.DecimalField(decimal_places=1, max_digits=25)),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=25)),
                ('humidity', models.IntegerField()),
                ('led1', models.BooleanField()),
                ('led2', models.BooleanField()),
                ('servo', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
