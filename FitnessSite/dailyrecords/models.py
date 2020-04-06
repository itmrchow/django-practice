from django.db import models
from items.models import ActionItem
from datetime import datetime


# Create your models here.
class DailyItem(models.Model):
    actionItem = models.ForeignKey(
        ActionItem, models.SET_NULL, blank=False, null=True)
    recordDate = models.DateTimeField('記錄日期', default=datetime.today())
    repes = models.IntegerField('次數')
    sets = models.IntegerField('組數')

    def __str__(self):
        return self.recordDate + '：' + self.repes+'x'+self.sets


class ItemRecord(models.Model):
    dailyItem = models.ForeignKey(
        DailyItem, models.SET_NULL, blank=False, null=True)
    weigth = models.FloatField('重量')
    repes = models.IntegerField('次數', null=True)
    remark = models.CharField("備註", max_length=20)
