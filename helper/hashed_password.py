from passlib.context import CryptContext # type: ignore

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashingPasswordHelper(password) -> str:
    return pwd_context.hash(password)

def chekHashingPassword(input_password: str, stored_hash: str) -> bool:
    return pwd_context.verify(input_password, stored_hash)
