# Generated by Django 3.0.2 on 2020-03-16 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200316_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartmodel',
            old_name='null',
            new_name='cart_id',
        ),
        migrations.RenameField(
            model_name='ordersmodel',
            old_name='null',
            new_name='cart_id',
        ),
    ]
