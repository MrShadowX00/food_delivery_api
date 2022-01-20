from pydantic import BaseModel
from typing import Optional



class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]
 
    class Config:
        orm_mode = True
        schema_extra={
            'example':{
                "username":"mirkhujaev",
                "email":"mirkhujaev@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }


class Settings(BaseModel):
    authjwt_secret_key:str = '9d5a92e5a7e1c0af8e6dbcceda9f633df99b3cd3e0143108b49c8d752ddb1729'

class LoginModel(BaseModel):
    username:str
    password:str

class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="LARGE"
    user_id:Optional[int]

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }


class OrderStatusModel(BaseModel):
    order_status:Optional[str]="PENDING"

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }

