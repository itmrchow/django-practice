from django.db import models
from parts.models import Part

from datetime import datetime


class ActionItem(models.Model):
    part = models.ForeignKey(
        Part,
        models.SET_NULL,
        blank=False,
        null=True,)
    item_name = models.CharField(max_length=20, null=True)
    create_date = models.DateTimeField('建立日期', default=datetime.today())
    modify_date = models.DateTimeField('修改日期', default=datetime.today())

    def __str__(self):
        return self.item_name
