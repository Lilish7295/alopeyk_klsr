# Generated by Django 4.2 on 2024-03-09 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AlterField(
            model_name='package',
            name='courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courier', to='user.customuser'),
        ),
        migrations.AlterField(
            model_name='package',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='user.customuser'),
        ),
        migrations.DeleteModel(
            name='Courier',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
