from django.db import models
from django.db.models.query_utils import Q

class RecordsManager(models.Manager):
    def create_record(self, device, record_dt, is_success, count):
        statistic = self.create(device=device, record_dt=record_dt, is_success=is_success, count=count)
        return statistic

    def search_by_device(self, device, start, end):
        records = self.filter(device=device, record_dt__range=(start, end))
        return records

    def search_by_time(self, start, end):
        records = self.filter(record_dt__range=(start, end))
        return records

class Records(models.Model):
    record_id = models.AutoField(primary_key=True)
    device = models.CharField(u'device', max_length=100)
    record_dt = models.DateTimeField()
    is_success = models.BooleanField()
    count = models.PositiveIntegerField()
    objects = RecordsManager()

    def __str__(self):  # __unicode__ on Python 2
        return '{}-{}'.format(self.record_id, self.device)

    class Meta:
        ordering = ['record_dt']
