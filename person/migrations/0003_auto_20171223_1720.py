# Generated by Django 2.0 on 2017-12-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20171223_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='p_gender',
            field=models.CharField(choices=[('M', 'පිරිමි'), ('F', 'ගැහැණු')], default='F', max_length=20, verbose_name='ස්ත්\u200dරී/ පුරුෂ භාවය'),
        ),
    ]