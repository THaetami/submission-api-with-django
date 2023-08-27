from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from server.utils.authentication_utils import decode_and_verify_jwt_token
from server.utils.mssalesman_utils import *

from .serialize import MssalesmenSerializers, MssalesmenViewSerializers
from .models import Mssalesmen


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
        
        check_and_return_penjualan_response(salesman.sal_id)
        
        salesman.delete()
        return Response({
            'status': 'success'
        }, status=204)