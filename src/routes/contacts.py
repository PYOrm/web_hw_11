from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.repository import contacts as repository_contacts
from src.schemas import ContactResponse, ContactModel

router = APIRouter(prefix="/contacts")


@router.get("/", response_model=list[ContactResponse])
async def read_contacts(name: str = None, soname: str = None, email: str = None, db: Session = Depends(get_db)):
    if name or soname or email:
        res = await repository_contacts.get_contact_(db, name=name, soname=soname, email=email)
    else:
        res = await repository_contacts.get_all_contacts(db)
    return res


@router.get("/{contact_id}", response_model=ContactResponse)
async def read_by_id(contact_id: int, db: Session = Depends(get_db)):
    return await repository_contacts.get_contact_by_id(db, contact_id)


@router.delete("/{contact_id}", response_model=ContactResponse)
async def remove_contact(contact_id: int, db=Depends(get_db)):
    return await repository_contacts.delete_contact(db, contact_id)


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_by_id(contact_id: int, body: ContactModel, db: Session = Depends(get_db)):
    return await repository_contacts.update_contact_by_id(db, contact_id, body)


@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    return await repository_contacts.create_contact(db, body)


@router.get("/upcoming_birthdays/", response_model=list[ContactResponse])
async def upcoming_birthdays(db: Session = Depends(get_db)):
    return await repository_contacts.get_upcoming_birthdays(db)
