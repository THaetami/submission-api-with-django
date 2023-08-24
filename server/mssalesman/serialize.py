from rest_framework import serializers
from .models import Mssalesmen

class MssalesmenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mssalesmen
        fields = '__all__'
        extra_kwargs = {
            'sal_kta_id': {'write_only': True}
        }
        