import asyncio
import jwt
from typing import Dict
from db.db_models import Users
from db_repo import UserRepo

user_repo = UserRepo()

SECRET = "avada-cedavra"
ALG = "HS256"



def create_token(data: Dict):
    return jwt.encode(data, SECRET, algorithm=ALG)

def decode_token(token: str):
    try:
        payload = jwt.decode(jwt=token, key=SECRET, algorithms=[ALG])
        login = payload.get("login")
        email = payload.get("email")
        token_decode = {
            "login": login,
            "email": email,
        }
        return token_decode
    except Exception as e:
        return e
    
    
async def user_token():
    user_data: Users = await user_repo.get_user(user_id=1)
    data = {
        "login": user_data.login,
        "email": user_data.email,        
    }
    token_encode = create_token(data=data)
    token_decode = decode_token(token=token_encode)
    print(f"""
###
Token encode: 
{token_encode}
###
Token decode:
login = {token_decode["login"]}
email = {token_decode["email"]}
    """
    )

if __name__ == "__main__":
    asyncio.run(user_token())
