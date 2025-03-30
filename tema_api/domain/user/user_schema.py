from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum


class Gender(str, Enum):
	M = 'M'
	F = 'F'

class UserEmail(BaseModel):
	userAccount: str
	email: EmailStr

class SubUser(BaseModel):
	name: str
	isMainUser: bool
	birthDay: datetime
	gender: Gender 
	weight:  float | None
	height: float | None 

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
   