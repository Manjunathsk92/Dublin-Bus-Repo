# Generated by Django 2.0.6 on 2018-08-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dublinBus', '0013_auto_20180808_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpoints',
            name='distance_travelled_on_DublinBus',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
