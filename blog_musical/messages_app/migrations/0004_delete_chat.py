# Generated by Django 4.0.5 on 2022-08-07 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messages_app', '0003_chat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
