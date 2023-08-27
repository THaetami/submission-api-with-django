from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Max
from django.http import Http404

from server.authentication_utils import decode_and_verify_jwt_token

from .serialize import MssalesmenSerializers, MssalesmenViewSerializers
from rest_framework.exceptions import AuthenticationFailed, NotFound, ValidationError
from .models import Mssalesmen
from mskota.models import Mskota
from trpenjualan.models import Trpenjualan


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
        
class Index(APIView):
    def get(self, request):
        
        decode_and_verify_jwt_token(request.COOKIES.get('jwt'))
         
        salesman = Mssalesmen.objects.all()
        serializer = MssalesmenViewSerializers(salesman, many=True)

        return Response({
            'status': 'success',
            'data': serializer.data
        })
    
class AddSales(APIView):
    def post(self, request):
        decode_and_verify_jwt_token(request.COOKIES.get('jwt'))
            
        get_kota(request.data.get('kota'))
        
        request.data['sal_id'] = generate_new_sal_id()

        serializer = MssalesmenSerializers(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'addedProduct': serializer.data
            }, status=201)
        else:
            return Response({
                'status': 'fail',
                'messages': serializer.errors,
            }, status=400)

class GetSalesById(APIView):
    def get(self, request, pk):
        decode_and_verify_jwt_token(request.COOKIES.get('jwt'))
        
        salesman = get_salesman(pk)
        
        serializer = MssalesmenViewSerializers(salesman, many=False)
        
        return Response({
            'status': 'success',
            'data': serializer.data
        })
    
class UpdateSales(APIView):
    def put(self, request, pk):
        decode_and_verify_jwt_token(request.COOKIES.get('jwt'))
        
        salesman = get_salesman(pk)
        
        get_kota(request.data.get('kota'))
        
        if salesman.sal_nm != request.data.get('sal_nm'):
            check_duplicate_name(pk, request.data.get('sal_nm'))
            
        check_bekerjasejak(pk, request.data['sal_bekerjasejak'])
        
        serializer = MssalesmenSerializers(salesman, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'updatedProduct': serializer.data
            })
        else:
            return Response({
                'status': 'false',
                'messages': serializer.errors
            }, status=400)


class DeleteSales(APIView):
    def delete(self, request, pk):
        decode_and_verify_jwt_token(request.COOKIES.get('jwt'))
        
        salesman = get_salesman(pk)
        
        penjualan = Trpenjualan.objects.filter(jul_sal=salesman)
        if penjualan.exists():
            return Response({
                'status': 'false',
                'messages': 'Sales tidak boleh dihapus karena memiliki penjualan'
            }, status=422)
        
        salesman.delete()
        return Response({
            'status': 'success'
        }, status=204)