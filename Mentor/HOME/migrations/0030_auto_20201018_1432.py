# Generated by Django 3.1 on 2020-10-18 09:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HOME', '0029_auto_20201018_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistdata',
            name='taskcreated',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 18, 14, 32, 45, 589944)),
        ),
        migrations.AlterField(
            model_name='todolistdata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
