# Generated by Django 3.1 on 2020-10-14 11:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HOME', '0002_userdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='UserProfile',
        ),
    ]
