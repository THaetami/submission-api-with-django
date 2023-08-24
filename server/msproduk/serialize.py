from rest_framework import serializers
from .models import Msproduk

class MsproduksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Msproduk
        fields = '__all__'
        extra_kwargs = {
            'prd_typ_id': {'write_only': True}
        }