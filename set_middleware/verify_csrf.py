from fastapi import Request, HTTPException, status, Depends

def verify_csrf(request: Request):
    # csrf_cookie = request.cookies.get("XSRF-TOKEN")
    csrf_header = request.headers.get("X-CSRF-Token")

    if not csrf_header:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing CSRF token"
        )