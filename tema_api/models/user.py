from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum

from database import Base


class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, autoincrement=True)
	user_account = Column(String, unique=True, nullable=False)
	password = Column(String, nullable=False)
	email = Column(String, unique=True, nullable=False)
	sns_account = Column(String)
	sns_type = Column(String)
	mobile_num = Column(String)
	create_dt = Column(DateTime, nullable=False)
	use_marketing = Column(Boolean)
	sub_users = relationship('SubUser', back_populates='user', cascade='all, delete')  
	
	def to_dict(self):
		'''
			Custom method to convert SQLAlchemy model to a dictionary
        '''
		return {column.name: getattr(self, column.name) for column in self.__table__.columns}
	#UserEnv      UserEnv     `gorm:"embedded" json:"userEnv,omitempty"`
	#SubUsers     []SubUser   `json:"subUserIds" gorm:"foreignKey:UserID;constraint:OnDelete:CASCADE;"`

class SubUser(Base):
	__tablename__ = 'sub_users'
	id = Column(Integer, primary_key=True, autoincrement=True)
	user_id =  Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
	user = relationship('User', back_populates='sub_users', foreign_keys=[user_id])
	uuid = Column(String, unique=True, nullable=False)
	is_main_user = Column(Boolean, nullable=False)
	name = Column(String)
	birth_day = Column(DateTime)
	gender = Column(Enum('M', 'W'), default='M', nullable=False)
	weight = Column(String)
	height = Column(String)
	image_path = Column(String)
	image_source = Column(String)
	create_dt = Column(DateTime, nullable=False)
	update_dt = Column(DateTime, nullable=False)

	def to_dict(self):
		'''
			Custom method to convert SQLAlchemy model to a dictionary
        '''
		return {column.name: getattr(self, column.name) for column in self.__table__.columns}

'''
type User struct {
	UserEnv      UserEnv     `gorm:"embedded" json:"userEnv,omitempty"`
}
'''

'''
type SubUser struct {
	IconIndex           *string      `json:"iconIndex,omitempty"`
	DeviceUuids         *StringArray `json:"deviceUuids,omitempty"`
	AlarmList           []UserAlarm  `json:"alarmList" gorm:"foreignKey:SubUserID;constraint:OnDelete:CASCADE;"`
	UserEnverment       SubUserEnv   `json:"userEnverment,omitempty"`
	IsLastSignIn        bool         `json:"isLastSignIn"`
	OtherDeviceUseSubId *string      `json:"-"`
	ShareLinks          []ShareLink  `json:"shareLinks" gorm:"foreignKey:SubUserID;constraint:OnDelete:CASCADE;"` // 新增的字段
}
'''