from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

class TimestampSerializer(serializers.Serializer):
    start = serializers.FloatField()
    end = serializers.FloatField()

class AudioProcessingRequestSerializer(serializers.Serializer):
    audio_file = serializers.FileField()
    timestamps = serializers.ListField(child=TimestampSerializer())
