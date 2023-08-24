from django.db import models

class Dtpenjualan(models.Model):
    djul_id = models.AutoField(primary_key=True)
    djul_jul = models.ForeignKey('trpenjualan.Trpenjualan', on_delete=models.CASCADE, db_column='djul_jul_id')
    djul_prd = models.ForeignKey('msproduk.MSProduk', on_delete=models.CASCADE, db_column='djul_prd_id')
    djul_qtyjual = models.FloatField(default=0)
    djul_hargasatuan = models.FloatField(default=0)

    class Meta:
        db_table = 'dtpenjualan'