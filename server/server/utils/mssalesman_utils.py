from mssalesman.models import Mssalesmen
from rest_framework.exceptions import NotFound, ValidationError


from trpenjualan.models import Trpenjualan


def get_salesman(pk):
    try:
        return Mssalesmen.objects.get(sal_id=pk)
    except Mssalesmen.DoesNotExist:
        raise NotFound({'status': 'fail', 'message': 'salesman tidak ditemukan'})

    
def check_and_return_penjualan_response(salesman):
    penjualan = Trpenjualan.objects.filter(jul_sal_id=salesman)
    if penjualan.exists():
        raise ValidationError({'status': 'fail', 'message': 'Sales tidak boleh dihapus karena memiliki penjualan.'})

    