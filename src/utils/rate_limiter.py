from slowapi import Limiter
from slowapi.util import get_remote_address

def getSessionUser(request):
    return request.session.get("user_id")

limiter = Limiter(key_func=getSessionUser)
