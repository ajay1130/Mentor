# Generated by Django 3.1 on 2020-11-17 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0050_auto_20201117_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followersandfollowing',
            name='created',
            field=models.DateField(default=datetime.datetime(2020, 11, 17, 18, 44, 44, 223320)),
        ),
        migrations.AlterField(
            model_name='todolistdata',
            name='taskcreated',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 17, 18, 44, 44, 222321)),
        ),
    ]
