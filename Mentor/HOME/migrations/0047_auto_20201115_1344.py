# Generated by Django 3.1 on 2020-11-15 08:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0046_auto_20201101_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistdata',
            name='taskcreated',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 13, 44, 38, 111794)),
        ),
    ]
