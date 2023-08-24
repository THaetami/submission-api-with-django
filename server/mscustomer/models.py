from django.db import models
from mskota.models import Mskota

class Mscustomer(models.Model):
    cus_id = models.CharField(max_length=4, primary_key=True)
    cus_nm = models.CharField(max_length=100)
    cus_tanggallahir = models.DateField(null=True, blank=True)
    cus_kta = models.ForeignKey(Mskota, on_delete=models.CASCADE, null=True, db_column='cus_kta_id')
    cus_aktif = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = 'mscustomer'

