from rest_framework import serializers
from .models import Mscustomer

class MscustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mscustomer
        fields = '__all__'
        extra_kwargs = {
            'cus_kta_id': {'write_only': True}
        }
        