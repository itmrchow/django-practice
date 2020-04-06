from django.db import models
from datetime import datetime
# Create your models here.


class Part(models.Model):
    part_txt = models.CharField(
        max_length=10, default='', unique=True, null=False, )
    part_name = models.CharField(max_length=10, default='', null=True)
    create_date = models.DateTimeField('建立日期', default=datetime.today())
    modify_date = models.DateTimeField('修改日期', default=datetime.today())

    def __str__(self):
        return self.part_name
