# Generated by Django 3.0.3 on 2020-03-06 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0002_auto_20200306_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 14, 23, 27, 136648), verbose_name='建立日期'),
        ),
        migrations.AlterField(
            model_name='part',
            name='modifyDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 14, 23, 27, 136648), verbose_name='修改日期'),
        ),
    ]
