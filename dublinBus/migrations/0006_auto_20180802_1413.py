# Generated by Django 2.0.6 on 2018-08-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dublinBus', '0005_userpoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpoints',
            name='dublin_bus_points',
            field=models.IntegerField(),
        ),
    ]
