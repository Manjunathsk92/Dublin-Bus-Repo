# Generated by Django 2.0.6 on 2018-08-07 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dublinBus', '0011_weatherforecast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpoints',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]