from fastapi import APIRouter, Depends # type: ignore
from controller.user_controller import UserController
from request.users_request import LogInRequest, RegisterRequest
from helper.hashed_password import hashingPasswordHelper
from auth.csrf import CsrfSettings, generate_csrf
from fastapi_csrf_protect import CsrfProtect

router = APIRouter()

class UserRoutes:
    @router.get("/root", status_code=200)
    def read_root():
        return UserController.status_server()
    
    @router.get("/csrf", status_code=200)
    def get_csrf(csrf_protect: CsrfProtect = Depends()):
        return generate_csrf(csrf_protect)

    @router.post("/register", status_code=200)
    def register(request: RegisterRequest):
        hashingPassword = hashingPasswordHelper(request.password)
        return UserController.CreatedUser(request.name, request.email, hashingPassword)

    @router.post("/login", status_code=200)
    def login_user(requestLogin: LogInRequest):
        return UserController.loginUser(requestLogin.email, requestLogin.password)

    @router.get("/users", status_code=200)
    def get_user():
        return UserController.get_all_users()
    
    @router.get("/users/{id}", status_code=200)
    def get_user_byId(id: int):
        return UserController.get_users_byId(id)
    