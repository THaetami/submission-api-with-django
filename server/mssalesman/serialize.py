from django.db.models import Max
from rest_framework import serializers
from trpenjualan.serialize import TrpenjualanSerializers
from rest_framework.exceptions import ValidationError

from .models import Mssalesmen
from mskota.models import Mskota
from trpenjualan.models import Trpenjualan
from mskota.serializer import MskotaSerializers

class MssalesmenCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mssalesmen
        fields = '__all__'
        read_only_fields = ('sal_id',) 
        
    def validate_kota(self, value):
        try:
            return Mskota.objects.get(kta_id=self.initial_data.get('kota'))
        except Mskota.DoesNotExist:
            raise ValidationError('Kota tidak ditemukan')
    
    def save(self, **kwargs):
        new_sal_id = self.generate_new_sal_id()
        self.validated_data['sal_id'] = new_sal_id
        return super().save(**kwargs)

    def generate_new_sal_id(self):
        last_salesman = Mssalesmen.objects.aggregate(max_sal_id=Max('sal_id'))
        last_sal_id = last_salesman['max_sal_id'] if last_salesman['max_sal_id'] is not None else None
        
        last_numeric_part = int(last_sal_id[1:]) if last_sal_id else 0
        new_numeric_part = last_numeric_part + 1
        new_sal_id = f"S{new_numeric_part:03}"
        
        return new_sal_id
        
        
class MssalesmenUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mssalesmen
        fields = '__all__'
    
    def validate_sal_bekerjasejak(self, value):
        sal_id = self.initial_data.get('sal_id') 
        penjualan = Trpenjualan.objects.filter(jul_sal_id=sal_id).order_by('jul_tanggaljual').first()

        if penjualan and value > penjualan.jul_tanggaljual:
            raise ValidationError('tanggal bekerja tidak benar.')
        return value
    
    def validate_kota(self, value):
        try:
            return Mskota.objects.get(kta_id=self.initial_data.get('kota'))
        except Mskota.DoesNotExist:
            raise ValidationError('Kota tidak ditemukan')


class MssalesmenViewSerializers(serializers.ModelSerializer):
    kota = MskotaSerializers(read_only=True) 
    penjualan = TrpenjualanSerializers(many=True, read_only=True)
    class Meta:
        model = Mssalesmen
        fields = '__all__'