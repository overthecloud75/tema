from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from enum import Enum


class Gender(str, Enum):
	M = 'M'
	F = 'F'

class TokenInfo(BaseModel):
	access_token: str
	token_type: str='Bearer'

class UserLogin(BaseModel):
	userAccount: str
	password: str
   
class UserRegister(BaseModel):
	userAccount: str
	email: EmailStr
	password: str
	useMarketing : bool = False

class SubUserResponse(BaseModel):
	userId: int
	uuid: str
	isMainUser: bool
	name: str
	birthDay: str
	gender: Gender
	weight: str | None
	height: str | None 
	createDt: datetime 
	updateDt: datetime

class UserResponse(BaseModel):
	snsAccount: str | None = None
	snsType: str | None = None
	mobileNum: str | None = None
	createDt: datetime
	useMarketing: bool | str       # ToBe : 향후 str은 없앨 예정 
	tokenInfo: TokenInfo
	subUserIds: list[SubUserResponse]
	