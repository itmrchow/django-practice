# Generated by Django 3.0.3 on 2020-03-09 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionitem',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 9, 15, 53, 9, 726761), verbose_name='建立日期'),
        ),
        migrations.AlterField(
            model_name='actionitem',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 9, 15, 53, 9, 726761), verbose_name='修改日期'),
        ),
    ]
