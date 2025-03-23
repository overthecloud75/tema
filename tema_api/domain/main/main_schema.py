from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
	userAccount: str
	password: str
   
class UserRegister(BaseModel):
	userAccount: str
	email: EmailStr
	password: str