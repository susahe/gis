# Generated by Django 2.0 on 2017-12-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20171223_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='p_edu',
            field=models.CharField(choices=[('PS', 'පාසල් යාමට පෙර'), ('PR', 'පෙර පාසැල්'), ('OF', '1-5 ශ්\u200dරේණිය දක්වා'), ('FO', '5 සිට සා/පෙළ දක්වා'), ('OP', 'සාමන්\u200dය පෙළ සමත්'), ('UA', 'උසස් පෙළ දක්වා'), ('AP', 'උසස් පෙළ සමත්'), ('DG', 'උපාධි හා ඊට ඉහල'), ('NS', 'කිසිදා පසැල් නොගිය')], default='OP', max_length=2, verbose_name='අධ්\u200dයාපන සුදුසුකම්'),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_gender',
            field=models.CharField(choices=[('M', 'පිරිමි'), ('F', 'ගැහැණු')], default='F', max_length=1, verbose_name='ස්ත්\u200dරී/ පුරුෂ භාවය'),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_job',
            field=models.CharField(max_length=50, verbose_name='රැකියාව'),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_job_position',
            field=models.CharField(max_length=50, verbose_name='තනතුර'),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_nationality',
            field=models.CharField(choices=[('SI', 'සිංහල'), ('TA', 'ද්\u200dරවිඩ'), ('MU', 'මුස්ලිම්'), ('BR', 'බර්ගර්'), ('MA', 'මැලේ'), ('OT', 'වෙනත්')], default='SI', max_length=2, verbose_name='ජාතිය'),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_nic',
            field=models.CharField(max_length=10, verbose_name='ජාතික හැඳුනුම්පත් අංකය'),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_religion',
            field=models.CharField(choices=[('BU', 'බෙද්ධ'), ('RC', 'කතෝලික'), ('HI', 'හින්දු'), ('IS', 'ඉස්ලාම්'), ('CH', 'ක්\u200dරිස්තියානි'), ('OT', 'වෙනත්')], default='BU', max_length=2, verbose_name='ඇාගම'),
        ),
    ]
