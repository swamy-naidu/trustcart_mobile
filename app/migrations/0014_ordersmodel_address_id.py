# Generated by Django 3.0.2 on 2020-03-31 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200331_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersmodel',
            name='address_id',
            field=models.IntegerField(default=False),
        ),
    ]
