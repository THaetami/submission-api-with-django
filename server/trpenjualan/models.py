from django.db import models

class Trpenjualan(models.Model):
    jul_id = models.AutoField(primary_key=True, unique=True)
    jul_tanggaljual = models.DateField()
    jul_sal = models.ForeignKey('mssalesman.Mssalesmen', on_delete=models.CASCADE, null=True, db_column='jul_sal_id')
    jul_cus = models.ForeignKey('mscustomer.Mscustomer', on_delete=models.CASCADE, null=True, db_column='jul_cus_id')
    jul_notes = models.CharField(max_length=100, null=True, blank=True)
    jul_tanggalbayar = models.DateField(null=True, blank=True, verbose_name='tanggal bayar')
    jul_batal = models.CharField(max_length=1, default='N', verbose_name='status pembatalan')

    class Meta:
        db_table = 'trpenjualan'
