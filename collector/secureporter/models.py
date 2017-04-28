from django.db import models
from django.db.models.query_utils import Q
from django.db.models import Count, Min, Sum, Avg

class RecordsManager(models.Manager):
    def create_record(self, device, record_dt, is_success, spent_seconds):
        statistic = self.create(device=device, record_dt=record_dt, is_success=is_success, spent_seconds=spent_seconds)
        return statistic

    def search_by_device(self, device, start, end):
        records = self.filter(device=device, record_dt__range=(start, end))
        return records

    def search_by_time(self, start, end):
        records = self.filter(record_dt__range=(start, end))
        return records

    def count_by_time(self, is_success, start, end):
        count = self.filter(is_succcess=is_success, record_dt__range=(start, end)).count()
        return count

    def fail_rate_by_time(self, start, end):
        fail = self.filter(is_success=False, record_dt__range=(start, end)).count()
        total = self.filter(record_dt__range=(start, end)).count()
        #totalsummary = self.filter(record_dt__range=(start, end)).aggregate(Sum('spent_seconds'))
        if total == 0:
            rate = None
        else:
            rate = fail / total

        return rate

class Records(models.Model):
    record_id = models.AutoField(primary_key=True)
    device = models.CharField(u'device', max_length=100)
    record_dt = models.DateTimeField()
    is_success = models.BooleanField()
    spent_seconds = models.FloatField(default=0)
    objects = RecordsManager()

    def __str__(self):  # __unicode__ on Python 2
        return '{}-{}'.format(self.record_id, self.device)

    class Meta:
        ordering = ['-record_dt']
