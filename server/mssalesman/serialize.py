from audioop import maxpp
from django import forms
from rest_framework import serializers
from trpenjualan.serialize import TrpenjualanSerializers
from datetime import datetime

from .models import Mssalesmen
from mskota.models import Mskota
from trpenjualan.models import Trpenjualan
from mskota.serializer import MskotaSerializers

class MssalesmenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mssalesmen
        fields = '__all__'

class MssalesmenViewSerializers(serializers.ModelSerializer):
    kota = MskotaSerializers(read_only=True) 
    penjualan = TrpenjualanSerializers(many=True, read_only=True)
    class Meta:
        model = Mssalesmen
        fields = '__all__'