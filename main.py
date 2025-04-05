from fastapi import FastAPI # type: ignore
from routes.routes import router
from set_middleware.token_middleware import TokenMiddleware

app = FastAPI()

app.include_router(router, prefix="/api/v1")
app.add_middleware(TokenMiddleware)


if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="127.0.0.1", port=2000)