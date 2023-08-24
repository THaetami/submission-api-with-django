from rest_framework import serializers
from .models import Mskota

class MskotaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mskota
        fields = '__all__'
        extra_kwargs = {
            'kta_id': {'write_only': True}
        }