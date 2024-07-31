from pydantic import BaseModel, Field, EmailStr, PastDate


class ContactModel(BaseModel):
    name: str = Field(max_length=50)
    soname: str = Field(max_length=50)
    email: EmailStr = Field(max_length=100)
    phone: str
    birthday: PastDate
    info: str = Field(max_length=255)


class ContactResponse(ContactModel):
    id: int

    class Config:
        from_attributes = True

