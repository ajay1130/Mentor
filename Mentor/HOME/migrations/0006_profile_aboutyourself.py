# Generated by Django 3.1 on 2020-10-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0005_auto_20201015_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aboutyourself',
            field=models.TextField(default=''),
        ),
    ]
