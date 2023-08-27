from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from server.authentication_utils import decode_and_verify_jwt_token
from .serializer import UserSerializer
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

def generate_jwt_token(user_id):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
    payload = {
        'id': user_id,
        'exp': expiration_time,
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token, expiration_time

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'addedUser': serializer.data
            }, status=201)
        return Response(serializer.errors, status=422)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('user not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        token, expiration_time = generate_jwt_token(user.id)
        
        response = Response()
        
        response.set_cookie(key='jwt', value=token, expires=expiration_time, httponly=True)
        
        response.data = {
            'message': 'login success'
        }
        
        return response
    
class UserView(APIView):
    def get(self, request):
        payload = decode_and_verify_jwt_token(request.COOKIES.get('jwt'))
        
        user = User.objects.get(id=payload['id'])
        
        serializer = UserSerializer(user)
        
        return Response({
            'status': 'success',
            'user': serializer.data
        })
    
class LogoutView(APIView):
    def delete(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response