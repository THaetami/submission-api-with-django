import jwt
from rest_framework.exceptions import AuthenticationFailed

def decode_and_verify_jwt_token(token):
    if not token:
        raise AuthenticationFailed('Unauthenticated')
    
    try: 
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token expired')
    except jwt.DecodeError:
        raise AuthenticationFailed('Token invalid')

