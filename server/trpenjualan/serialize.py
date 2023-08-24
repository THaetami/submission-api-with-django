from rest_framework import serializers
from .models import Trpenjualan

class TrpenjualanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trpenjualan
        fields = '__all__'
        extra_kwargs = {
            'jul_sal_id': {'write_only': True},
            'jul_cus_id': {'write_only': True},
        }