# auth/csrf.py

from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
from fastapi.responses import JSONResponse
from pydantic_settings import BaseSettings
from fastapi import Depends

# Config settings
class CsrfSettings(BaseSettings):
    secret_key: str = "asecrettoeverybody"
    cookie_samesite: str = "lax"

@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()

# Generate CSRF token
def generate_csrf(csrf_protect: CsrfProtect = Depends()):
    csrf_token, signed_token = csrf_protect.generate_csrf_tokens()
    response = JSONResponse(content={"csrf_token": csrf_token})
    csrf_protect.set_csrf_cookie(signed_token, response)
    return response
