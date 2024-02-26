# Generated by Django 4.2 on 2024-02-26 08:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12)),
                ('condition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('adress', models.TextField()),
                ('phone_number', models.CharField(max_length=12)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
                ('registery_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_long', models.DecimalField(decimal_places=6, default=datetime.datetime(2024, 2, 26, 8, 41, 11, 705969, tzinfo=datetime.timezone.utc), max_digits=9)),
                ('origin_lat', models.DecimalField(decimal_places=6, default=datetime.datetime(2024, 2, 26, 8, 41, 11, 705969, tzinfo=datetime.timezone.utc), max_digits=9)),
                ('destination_long', models.DecimalField(decimal_places=6, default=datetime.datetime(2024, 2, 26, 8, 41, 11, 705969, tzinfo=datetime.timezone.utc), max_digits=9)),
                ('destination_lat', models.DecimalField(decimal_places=6, default=datetime.datetime(2024, 2, 26, 8, 41, 11, 705969, tzinfo=datetime.timezone.utc), max_digits=9)),
                ('status', models.CharField(choices=[('waiting', 'منتظر قبول پبک'), ('the_way_to_pickup', 'پیک در راه مبدا'), ('the_way_to_deliver', 'پیک در راه مقصد'), ('delivered', 'انجام شد'), ('canceled', 'لغو شد')], default='waiting', max_length=30)),
                ('pick_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deliver_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('condition', models.TextField()),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.courier')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1 - very bad'), (2, '2 - bad'), (3, '3 - avrage'), (4, '4 - good'), (5, '5 - excellent')], default=1)),
                ('comments', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.package')),
            ],
        ),
    ]