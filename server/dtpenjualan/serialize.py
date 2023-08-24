from rest_framework import serializers
from .models import Dtpenjualan

class DtpenjualanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dtpenjualan
        fields = '__all__'
        extra_kwargs = {
            'djul_jul_id': {'write_only': True},
            'djul_prd_id': {'write_only': True},
        }