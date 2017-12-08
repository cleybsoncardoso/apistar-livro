from apistar_jwt.authentication import JWTAuthentication, get_jwt
from apistar_jwt.token import JWT
from apistar.interfaces import Auth, Schema
from apistar import http, annotate
import jwt

def get_token():
    payload = {'user': 2, 'username': 'fdfdfdfd', 'SECRET': 'jwt-secret'}
    secret = 'jwt-secret'
    encoded_jwt = jwt.encode(
        payload, secret, algorithm='HS256').decode(encoding='UTF-8')
    return {'Authorization': 'Bearer {token}'.format(token=encoded_jwt)}

@annotate(authentication=[JWTAuthentication()])
def auth_required(request: http.Request, auth: Auth):
    return auth.user


def injected_component(request: http.Request, token: JWT):
    return token.payload
