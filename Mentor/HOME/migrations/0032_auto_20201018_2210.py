# Generated by Django 3.1 on 2020-10-18 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0031_auto_20201018_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='todolistdata',
            name='taskcreated',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 18, 22, 10, 42, 826917)),
        ),
    ]
