# Generated by Django 3.1.1 on 2021-04-07 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_remove_incident_sub_incident_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='Sub_Incident_Type',
            field=models.CharField(choices=[('1', 'Environmental_Incident'), ('2', 'Injurry//Illness'), ('3', 'Property_Damage'), ('4', 'Vehicle')], default='2', max_length=2),
        ),
    ]
