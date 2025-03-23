from sqlalchemy import Column, Integer, String, Text, DateTime

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
    use_marketing = Column(DateTime)
	#TokenInfo    *TokenModel `gorm:"embedded" json:"tokenInfo,omitempty"`
	#UserEnv      UserEnv     `gorm:"embedded" json:"userEnv,omitempty"`
	#SubUsers     []SubUser   `json:"subUserIds" gorm:"foreignKey:UserID;constraint:OnDelete:CASCADE;"`

'''
type User struct {
	ID           *uint       `json:"id,omitempty"`
	UserAccount  string      `json:"userAccount" gorm:"unique"`
	Password     string      `json:"password"`
	Email        string      `json:"email"`
	SnsAccount   *string     `json:"snsAccount,omitempty"`
	SnsType      *string     `json:"snsType,omitempty"`
	MobileNum    *string     `json:"mobileNum,omitempty"`
	CreateDt     *CustomTime `json:"createDt,omitempty"`
	UseMarketing *CustomTime `json:"useMarketing,omitempty"`
	TokenInfo    *TokenModel `gorm:"embedded" json:"tokenInfo,omitempty"`
	UserEnv      UserEnv     `gorm:"embedded" json:"userEnv,omitempty"`
	SubUsers     []SubUser   `json:"subUserIds" gorm:"foreignKey:UserID;constraint:OnDelete:CASCADE;"`
}
'''