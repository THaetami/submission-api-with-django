from django.db import models

class Mstypeproduk(models.Model):
    typ_id = models.CharField(max_length=3, primary_key=True)
    typ_nm = models.CharField(max_length=100)
    typ_persenkomisi = models.FloatField(default=0)
    typ_notes = models.CharField(max_length=1000, null=True, blank=True)
    typ_aktif = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = 'mstypeproduk'
