from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .serialize import MssalesmenSerializers
from .models import Mssalesmen

class Index(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('unauthenticated')
        
        products = Mssalesmen.objects.all()
        serializer = MssalesmenSerializers(products, many=True)

        response_data = {
            'status': 'success',
            'data': serializer.data
        }
        return Response(response_data)
    
class AddSales(APIView):
    def post(self, request):
        pass

class GetSalesById(APIView):
    def get(self, request):
        pass
    
class UpdateSales(APIView):
    def put(self, request):
        pass
    
class DeleteSales(APIView):
    def delete(self, request):
        pass