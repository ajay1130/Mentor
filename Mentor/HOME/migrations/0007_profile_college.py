# Generated by Django 3.1 on 2020-10-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0006_profile_aboutyourself'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='college',
            field=models.TextField(default=''),
        ),
    ]
