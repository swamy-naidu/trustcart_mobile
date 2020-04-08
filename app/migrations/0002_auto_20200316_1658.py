# Generated by Django 3.0.2 on 2020-03-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('idno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('model_no', models.CharField(max_length=40, unique=True)),
                ('category', models.CharField(max_length=50)),
                ('null', models.IntegerField(default=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrdersModel',
            fields=[
                ('idno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('model_no', models.CharField(max_length=40, unique=True)),
                ('category', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('total', models.FloatField()),
                ('null', models.IntegerField(default=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='laptopsmodel',
            name='hdd_capacity',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='camerasmodel',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='laptopsmodel',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='laptopsmodel',
            name='sales_package',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mobilesmodel',
            name='in_the_box',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mobilesmodel',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='telivisionsmodel',
            name='price',
            field=models.FloatField(),
        ),
    ]
