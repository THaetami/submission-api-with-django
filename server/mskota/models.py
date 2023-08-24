from django.db import models

class Mskota(models.Model):
    kta_id = models.CharField(max_length=3, primary_key=True)
    kta_nm = models.CharField(max_length=100)
    kta_notes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'mskota'
