from django.db import models
from django.db.models.query_utils import Q
from django.db.models import Count, Min, Sum, Avg

class RecordsManager(models.Manager):
    def create_record(self, device, record_dt, is_success, spent_seconds):
        statistic = self.create(device=device, record_dt=record_dt, \
                        is_success=is_success, spent_seconds=spent_seconds)
        return statistic

    def search_by_time(self, device, start, end):
        if device is None:
            records = self.filter(record_dt__gte=start, record_dt__lt=end)
        else:
            records = self.filter(device=device, record_dt__gte=start, record_dt__lt=end)
        return records

    def fail_rate_by_time(self, device, start, end):
        if device is None:
            fail = self.filter(is_success=False, record_dt__gte=start, record_dt__lt=end).count()
            total = self.filter(record_dt__gte=start, record_dt__lt=end).count()
        else:
            fail = self.filter(device=device, is_success=False, \
                    record_dt__gte=start, record_dt__lt=end).count()
            total = self.filter(device=device, record_dt__gte=start, record_dt__lt=end).count()

        if total == 0:
            rate = None
        else:
            rate = fail / total

        return rate

    def response_by_time(self, device, start, end):
        if device is None:
            avg_response_seconds = self.filter(is_success=True, record_dt__gte=start, \
                                    record_dt__lt=end)
        else:
            avg_response_seconds = self.filter(device=device, is_success=True, \
                                     record_dt__gte=start, record_dt__lt=end)

        return avg_response_seconds

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
