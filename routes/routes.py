from fastapi import APIRouter # type: ignore
from controller.user_controller import UserController
from request.users_request import LogInRequest, RegisterRequest
from helper.hashed_password import hashingPasswordHelper

router = APIRouter()


class UserRoutes:
    @router.get("/root", status_code=200)
    def read_root():
        return UserController.status_server()
    
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
    