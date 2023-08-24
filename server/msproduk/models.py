from django.db import models

class Msproduk(models.Model):
    prd_id = models.CharField(max_length=5, primary_key=True)
    prd_nm = models.CharField(max_length=100)
    prd_typ = models.ForeignKey('mystypeproduk.Mstypeproduk', on_delete=models.CASCADE, null=True, db_column='prd_typ_id')
    prd_aktif = models.CharField(max_length=1, default='Y')
    prd_notes = models.CharField(max_length=1000, null=True, blank=True)
    prd_hargamodal = models.FloatField(null=True, blank=True)
    prd_stokawal = models.FloatField(default=0)

    class Meta:
        db_table = 'msproduk'
