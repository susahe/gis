# Generated by Django 2.0 on 2017-12-24 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_auto_20171223_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='p_pic',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
