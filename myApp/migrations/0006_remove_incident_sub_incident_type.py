# Generated by Django 3.1.1 on 2021-04-07 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_auto_20210407_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='Sub_Incident_Type',
        ),
    ]
