from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from server.utils.authentication_utils import decode_and_verify_jwt_token
from server.utils.mssalesman_utils import *

from .serialize import *
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
        
        serializer = MssalesmenCreateSerializers(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'addedSales': serializer.data
            }, status=201)
        return Response({
            'status': 'fail',
            'messages': serializer.errors,
        }, status=422)


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
        
        request.data['sal_id'] = salesman.sal_id
        
        serializer = MssalesmenUpdateSerializers(salesman, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'updatedSales': serializer.data
            })
        return Response({
            'status': 'false',
            'messages': serializer.errors
        }, status=422)


class DeleteSales(APIView):
    def delete(self, request, pk):
        decode_and_verify_jwt_token(request.COOKIES.get('jwt'))
        
        salesman = get_salesman(pk)
        
        check_and_return_penjualan_response(salesman.sal_id)
        
        salesman.delete()
        return Response({
            'status': 'success'
        }, status=204)