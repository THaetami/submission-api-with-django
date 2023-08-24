from django.db import models

class Mssalesmen(models.Model):
    sal_id = models.CharField(max_length=4, primary_key=True)
    sal_nm = models.CharField(max_length=100)
    sal_bekerjasejak = models.DateField(null=True, blank=True)
    sal_aktif = models.CharField(max_length=1, default='Y', null=False)
    sal_kta = models.ForeignKey('mskota.Mskota', on_delete=models.CASCADE, null=True, db_column='sal_kta_id')

    class Meta:
        db_table = 'mssalesmen'