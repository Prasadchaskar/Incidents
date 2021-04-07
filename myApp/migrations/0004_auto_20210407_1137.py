# Generated by Django 3.1.1 on 2021-04-07 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0003_auto_20210407_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='Initial_Severity',
            field=models.SmallIntegerField(choices=[(1, 'Mild'), (2, 'Modarate'), (3, 'Severe'), (4, 'Fatal')]),
        ),
        migrations.AlterField(
            model_name='incident',
            name='Reportes_By',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='incident',
            name='suspected_Cause',
            field=models.TextField(),
        ),
    ]