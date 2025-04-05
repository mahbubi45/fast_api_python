from typing import List
from model.user_model import UserModel

class Responses:
    @staticmethod
    def response_user_list(message: str, status: int, data: List[UserModel] = []):
        return {
            "message": message,
            "status": status,
            "data": data
        }
    
    @staticmethod
    def response_login(message: str, status: int, token: str):
        return {
            "message": message,
            "status": status,
            "token": token,
            # "data": data
        }

    @staticmethod
    def response_user_detail(message: str, status: int, data: UserModel):
        return {
            "message": message,
            "status": status,
            "data": data
        }
    
