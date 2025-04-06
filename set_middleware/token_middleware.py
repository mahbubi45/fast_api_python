from fastapi import Request # type: ignore
from starlette.middleware.base import BaseHTTPMiddleware # type: ignore
from fastapi.responses import JSONResponse # type: ignore
from jose import jwt, JWTError # type: ignore
from datetime import datetime, timezone
from dotenv import load_dotenv # type: ignore
import os

class TokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        load_dotenv()
        SECRET_KEY = os.getenv("SECRET_KEY")
        ALGORITHM = os.getenv("ALGORITHM")

        base_path= "/api/v1/"
        # tanpa jwt token
        public_paths = ["login", "register", "docs", "openapi.json", "csrf"]
        allowed_path = [f"{base_path}{path}" for path in public_paths]
        
        if any(request.url.path.startswith(path) for path in allowed_path):
            return await call_next(request)

        # Ambil token dari header
        auth_header = request.headers.get("Authorization")
        print("AUTH HEADER:", auth_header)
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse({"detail": "Unauthorized - Token missing"}, status_code=401)

        token = auth_header.split(" ")[1]
        
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            exp = payload.get("exp")
            if exp and datetime.fromtimestamp(exp, tz=timezone.utc) < datetime.now(timezone.utc):
                return JSONResponse({"detail": "Token expired"}, status_code=401)

            # Simpan payload di request.state supaya bisa diakses di route
            request.state.user = payload

        except JWTError:
            return JSONResponse({"detail": "Unauthorized - Invalid token"}, status_code=401)

        return await call_next(request)
