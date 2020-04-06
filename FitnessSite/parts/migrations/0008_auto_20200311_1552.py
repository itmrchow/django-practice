# Generated by Django 3.0.3 on 2020-03-11 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0007_auto_20200309_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 11, 15, 52, 11, 915120), verbose_name='建立日期'),
        ),
        migrations.AlterField(
            model_name='part',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 11, 15, 52, 11, 915120), verbose_name='修改日期'),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_txt',
            field=models.CharField(default='部位', max_length=10, unique=True),
        ),
    ]
