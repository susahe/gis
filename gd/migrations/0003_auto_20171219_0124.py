# Generated by Django 2.0 on 2017-12-19 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gd', '0002_auto_20171219_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gramasevadivision',
            name='gs_village',
            field=models.CharField(max_length=300, verbose_name='ගම'),
        ),
    ]
