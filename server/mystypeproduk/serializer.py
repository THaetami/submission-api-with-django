from rest_framework import serializers
from .models import Mstypeproduk

class MstypeprodukSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mstypeproduk
        fields = '__all__'
        extra_kwargs = {
            'typ_id': {'write_only': True}
        }