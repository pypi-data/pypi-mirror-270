from rest_framework import serializers
from .models import  Water, WaterCli
from datetime import datetime

class CustomDateTimeField(serializers.DateTimeField):
    def to_internal_value(self, data):
        datetime_obj = datetime.strptime(data, "%Y%m%d%H%M")
        return super().to_internal_value(datetime_obj)

    def to_representation(self, value):
        formatted_datetime = value.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_datetime

class WaterSerializer(serializers.ModelSerializer):
    data_time = CustomDateTimeField()

    class Meta:
        model = Water
        fields = ['data_time', 'ma_q']

class CliSerializer(serializers.ModelSerializer):
    data_time = CustomDateTimeField()

    class Meta:
        model = WaterCli
        fields = ['data_time', 'ma_q', 'temp', 'humodity', 'atmo', 'floor', 'hr']