# Generated by Django 3.1 on 2020-10-27 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0034_auto_20201026_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistdata',
            name='taskcreated',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 21, 44, 10, 631933)),
        ),
    ]
