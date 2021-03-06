# Generated by Django 3.0.3 on 2020-03-06 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0003_auto_20200306_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part',
            old_name='partName',
            new_name='part_name',
        ),
        migrations.RenameField(
            model_name='part',
            old_name='partTxt',
            new_name='part_txt',
        ),
        migrations.RemoveField(
            model_name='part',
            name='createDate',
        ),
        migrations.RemoveField(
            model_name='part',
            name='modifyDate',
        ),
        migrations.AddField(
            model_name='part',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 14, 32, 40, 471136), verbose_name='建立日期'),
        ),
        migrations.AddField(
            model_name='part',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 14, 32, 40, 471136), verbose_name='修改日期'),
        ),
    ]
