from django.db import models
from mskota.models import Mskota
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator


class Mssalesmen(models.Model):
    alphabetic_space_validator = RegexValidator(
        regex=r'^[a-zA-Z ]*$',
        message='Only alphabetic characters and spaces are allowed.',
    )
    
    sal_id = models.CharField(max_length=4, primary_key=True, blank=False)
    sal_nm = models.CharField(max_length=100, blank=False, unique=True, validators=[MinLengthValidator(3), alphabetic_space_validator] )
    sal_bekerjasejak = models.DateField(null=True, blank=False)
    sal_aktif = models.CharField(max_length=1, default='Y', null=False)
    kota = models.ForeignKey(Mskota, on_delete=models.CASCADE, null=True, blank=False, db_column='sal_kta_id')

    class Meta:
        db_table = 'mssalesmen'
        