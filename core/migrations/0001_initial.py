# Generated by Django 5.0.6 on 2024-06-13 06:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('cell', models.CharField(default='+263776149765', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NetworkTraffic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('protocol_type', models.CharField(max_length=10)),
                ('service', models.CharField(max_length=50)),
                ('flag', models.CharField(max_length=10)),
                ('src_bytes', models.IntegerField()),
                ('dst_bytes', models.IntegerField()),
                ('land', models.BooleanField()),
                ('wrong_fragment', models.IntegerField()),
                ('urgent', models.IntegerField()),
                ('hot', models.IntegerField()),
                ('num_failed_logins', models.IntegerField()),
                ('logged_in', models.BooleanField()),
                ('num_compromised', models.IntegerField()),
                ('root_shell', models.BooleanField()),
                ('su_attempted', models.IntegerField()),
                ('num_root', models.IntegerField()),
                ('num_file_creations', models.IntegerField()),
                ('num_shells', models.IntegerField()),
                ('num_access_files', models.IntegerField()),
                ('num_outbound_cmds', models.IntegerField()),
                ('is_host_login', models.BooleanField()),
                ('is_guest_login', models.BooleanField()),
                ('count', models.IntegerField()),
                ('srv_count', models.IntegerField()),
                ('serror_rate', models.FloatField()),
                ('srv_serror_rate', models.FloatField()),
                ('rerror_rate', models.FloatField()),
                ('srv_rerror_rate', models.FloatField()),
                ('same_srv_rate', models.FloatField()),
                ('diff_srv_rate', models.FloatField()),
                ('srv_diff_host_rate', models.FloatField()),
                ('dst_host_count', models.IntegerField()),
                ('dst_host_srv_count', models.IntegerField()),
                ('dst_host_same_srv_rate', models.FloatField()),
                ('dst_host_diff_srv_rate', models.FloatField()),
                ('dst_host_same_src_port_rate', models.FloatField()),
                ('dst_host_srv_diff_host_rate', models.FloatField()),
                ('dst_host_serror_rate', models.FloatField()),
                ('dst_host_srv_serror_rate', models.FloatField()),
                ('dst_host_rerror_rate', models.FloatField()),
                ('dst_host_srv_rerror_rate', models.FloatField()),
                ('outcome', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Network Traffic',
                'verbose_name_plural': 'Network Traffic',
                'ordering': ('-created_at',),
            },
        ),
    ]
