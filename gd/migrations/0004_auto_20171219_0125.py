# Generated by Django 2.0 on 2017-12-19 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gd', '0003_auto_20171219_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gramasevadivision',
            name='gs_division',
            field=models.CharField(max_length=300, verbose_name='ග්\u200dරාම නිලධාරි වසම'),
        ),
    ]
