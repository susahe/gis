# Generated by Django 2.0 on 2017-12-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gd', '0004_auto_20171219_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gramasevadivision',
            name='gs_road',
            field=models.CharField(max_length=300, verbose_name='පාර'),
        ),
    ]
