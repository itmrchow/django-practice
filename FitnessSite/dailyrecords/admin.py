from django.contrib import admin
from .models import DailyItem, ItemRecord

# Register your models here.
admin.site.register(DailyItem)
admin.site.register(ItemRecord)
