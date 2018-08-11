# Generated by Django 2.0.6 on 2018-08-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dublinBus', '0007_auto_20180802_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weatherdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_date', models.CharField(max_length=20)),
                ('rain', models.DecimalField(decimal_places=18, max_digits=20)),
                ('temp', models.DecimalField(decimal_places=18, max_digits=20)),
                ('wetb', models.DecimalField(decimal_places=18, max_digits=20)),
                ('dewpt', models.DecimalField(decimal_places=18, max_digits=20)),
                ('vappr', models.DecimalField(decimal_places=18, max_digits=20)),
                ('rhum', models.IntegerField()),
                ('msl', models.DecimalField(decimal_places=18, max_digits=20)),
            ],
        ),
    ]
