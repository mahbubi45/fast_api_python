from fastapi import FastAPI, status # type: ignore
from database import mydb
from response.response import Responses
from helper.hashed_password import chekHashingPassword
from jwt_token.token import created_access_token

app = FastAPI()
# Create a cursor object
cursor = mydb.cursor(dictionary=True)

class UserController:
    # Create a cursor object
    @staticmethod
    def status_server():
        return {
             "status": 200,
             "message": "Server Aktived"
         }
    
    @staticmethod
    def chekPassword(password: str) -> bool:
        query = "SELECT * FROM users WHERE password = %s"
        cursor.execute(query, (password,))
        results = cursor.fetchone()

        return results is not None
    
    @staticmethod
    def chekEmail(email: str) -> bool:
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        results = cursor.fetchone()

        return results is not None

    @staticmethod
    def CreatedUser(name: str, email :str, password: str):
        insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (name, email, password))
        mydb.commit()

        return Responses.response_user_detail(
            message="Success",
            status=status.HTTP_200_OK,
            data=cursor.lastrowid
        )
    
    @staticmethod
    def loginUser(email: str, password: str):
        select_query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(select_query, (email,))
        results = cursor.fetchone()

        if not UserController.chekEmail(email): # type: ignore
            return Responses.response_login(
              message="Email Salah",
              status=status.HTTP_400_BAD_REQUEST,
            #   data=None,
              token=None
        )

        hashPassword = results["password"]

        if not chekHashingPassword(password, hashPassword): # type: ignore
            return Responses.response_login(
                message="Password Salah",
                status=status.HTTP_400_BAD_REQUEST,
                # data=None,
                token=None
            )
        
        if not results:
             return  Responses.response_login(
                 message="Email Atau Password Salah",
                 status=status.HTTP_404_NOT_FOUND,
                #  data=None,
                 token=None
             )

        token = created_access_token({"id": results["id"]})
        return Responses.response_login(
            message="Success Login",
            status=status.HTTP_200_OK,
            # data=results,
            token=token
        )

    @staticmethod
    def get_all_users():
        select_query = "SELECT * FROM users"
        cursor.execute(select_query)
        results = cursor.fetchall()

        if not results:
            return Responses.response_user_list(
                    message="404",
                    status=status.HTTP_404_NOT_FOUND,
                    data=results)
        
        # bisa mapping lewat kek gini tanpa model
        # for user in results:
        #     user.pop("id")
        #     user.pop("password")

        return Responses.response_user_list(
            message="Success",
            status=status.HTTP_200_OK,
            data=results)
    
    @staticmethod
    def get_users_byId(id: int):
       select_query = "SELECT * FROM users WHERE id = %s"
       cursor.execute(select_query, (id,))
       results = cursor.fetchone()

       return Responses.response_user_detail(
           message="Success",
           status=status.HTTP_200_OK,
           data=results
       )