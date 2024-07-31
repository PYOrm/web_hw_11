from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    soname = Column(String(50), nullable=False)
    email = Column(String(100))
    phone = Column("phone_number", String(30))
    birthday = Column("birth_day", Date)
    info = Column("Info", String(250), nullable=True)
