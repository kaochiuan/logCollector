from django.core.exceptions import MultipleObjectsReturned
from rest_framework import serializers
from secureporter.models import Records

class RecordSerializer(serializers.ModelSerializer):
    def create(self, data):
        try:
            record = Records.objects.create_record(
                device=data['device'],
                record_dt=data['record_dt'],
                is_success=data['is_success'],
                count=data['count'])
        except MultipleObjectsReturned:
            record = None
        return record

    class Meta:
        model = Records
        fields = ('record_id', 'device', 'record_dt', 'is_success', 'count',)
        read_only_fields = ('record_id',)