# Generated by Django 3.1 on 2020-10-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0017_delete_todolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABCD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
