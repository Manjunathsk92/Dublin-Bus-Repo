# Generated by Django 2.0.6 on 2018-07-31 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dublinBus', '0003_userfavourites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavourites',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
