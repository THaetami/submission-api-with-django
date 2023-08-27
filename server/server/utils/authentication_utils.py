import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed

def decode_and_verify_jwt_token(token):
    if not token:
        raise AuthenticationFailed('Unauthenticated')
    
    try: 
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        print(payload)
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token expired')
    except jwt.DecodeError:
        raise AuthenticationFailed('Token invalid')
    
def generate_jwt_token(user_id):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
    payload = {
        'id': user_id,
        'exp': expiration_time,
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token, expiration_time

