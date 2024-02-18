import jwt
from typing import Dict
from db_repo import UserRepo

user_repo = UserRepo()

SECRET = "avada-cedavra"
ALG = "HS256"



def create_token(data: Dict):
    return jwt.encode(data, SECRET, algorithm=ALG)

def user_token():
    user_data = user_repo.

if __name__ == "__main__":
    
