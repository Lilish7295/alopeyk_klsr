# Generated by Django 4.2 on 2024-02-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_alter_package_destination_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='destination_lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='destination_long',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='origin_lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='origin_long',
            field=models.FloatField(),
        ),
    ]
