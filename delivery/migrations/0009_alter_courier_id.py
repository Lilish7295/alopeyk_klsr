# Generated by Django 4.2 on 2024-03-05 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0008_alter_courier_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]