from django.core.exceptions import MultipleObjectsReturned
from rest_framework import serializers
from secureporter.models import Records

class RecordSerializer(serializers.ModelSerializer):
    record_dt = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S%Z")

    def create(self, data):
        try:
            record = Records.objects.create_record(
                device=data['device'],
                record_dt=data['record_dt'],
                is_success=data['is_success'],
                spent_seconds=data['spent_seconds'])
        except MultipleObjectsReturned:
            record = None
        return record

    class Meta:
        model = Records
        fields = ('record_id', 'device', 'record_dt', 'is_success', 'spent_seconds',)
        read_only_fields = ('record_id',)
