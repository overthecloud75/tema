from pydantic import BaseModel, EmailStr

class UserEmail(BaseModel):
	userAccount: str
	email: EmailStr
   