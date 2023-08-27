from mssalesman.models import Mssalesmen
from rest_framework.exceptions import NotFound, ValidationError
from datetime import datetime


from mskota.models import Mskota
from trpenjualan.models import Trpenjualan
from django.db.models import Max



def generate_new_sal_id():
    last_salesman = Mssalesmen.objects.aggregate(max_sal_id=Max('sal_id'))
    last_sal_id = last_salesman['max_sal_id'] if last_salesman['max_sal_id'] is not None else None
    
    last_numeric_part = int(last_sal_id[1:]) if last_sal_id else 0
    new_numeric_part = last_numeric_part + 1
    new_sal_id = f"S{new_numeric_part:03}"
    
    return new_sal_id

def get_salesman(pk):
    try:
        return Mssalesmen.objects.get(sal_id=pk)
    except Mssalesmen.DoesNotExist:
        raise NotFound({'status': 'fail', 'message': 'salesman tidak ditemukan'})

def get_kota(kota_id):
    try:
        return Mskota.objects.get(kta_id=kota_id)
    except Mskota.DoesNotExist:
        raise NotFound({'status': 'fail', 'message': 'kota tidak ditemukan'})

def check_duplicate_name(sal_id, sal_nm):
    if Mssalesmen.objects.exclude(sal_id=sal_id).filter(sal_nm=sal_nm).exists():
        raise ValidationError({'status': 'fail', 'message': 'Nama sudah digunakan oleh sales lain.'})

def check_bekerjasejak(jul_sal_id, sal_bekerjasejak_str):
    penjualan = Trpenjualan.objects.filter(jul_sal_id=jul_sal_id).order_by('jul_tanggaljual').first()
    sal_bekerjasejak = datetime.strptime(sal_bekerjasejak_str, '%Y-%m-%d').date()

    if penjualan and sal_bekerjasejak > penjualan.jul_tanggaljual :
        raise ValidationError({'status': 'fail', 'message': 'tanggal bekerja tidak benar.'})
    
def check_and_return_penjualan_response(salesman):
    penjualan = Trpenjualan.objects.filter(jul_sal_id=salesman)
    if penjualan.exists():
        raise ValidationError({'status': 'fail', 'message': 'Sales tidak boleh dihapus karena memiliki penjualan.'})

    