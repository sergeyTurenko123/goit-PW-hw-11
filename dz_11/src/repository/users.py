from typing import List

from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas import UsersBase, UsersStatusUpdate
import datetime  as dt
from datetime import datetime  as dtdt

async def get_users(skip: int, limit: int, db: Session) -> List[User]:
    users = db.query(User).offset(skip).limit(limit).all()
    now = dtdt.today().date()
    birthdays = []
    for user in users:
        date_user = user.date_of_birth
        week_day = date_user.isoweekday()
        difference_day = (date_user.day - now.day)
        if 1 <= difference_day < 7 :
            if difference_day < 6 :
                birthdays.append(user)
            else:
                if difference_day == 7:
                    birthdays.append(user)
                elif difference_day == 6:
                    birthdays.append(user)
    return birthdays
        
async def get_user(user_id: int, db: Session) -> User:
    return db.query(User).filter(User.id == user_id).first()

async def get_user_name(name: str, surname:str, email_address:str, phone_number: str, db: Session) -> User:
    if name:
        return db.query(User).filter(User.name == name).first()
    elif surname:
        return db.query(User).filter(User.surname == surname).first()
    elif email_address:
        return db.query(User).filter(User.email_address == email_address).first()
    elif phone_number:
        return db.query(User).filter(User.phone_number== phone_number).first()

async def create_user(body: UsersBase, db: Session) -> User:
    user = User(name=body.name, surname=body.surname, email_address=body.email_address, phone_number=body.phone_number, date_of_birth = body.date_of_birth, additional_data = body.additional_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

async def remove_user(user_id: int, db: Session) -> User | None:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


async def update_user(user_id: int, body: UsersBase, db: Session) -> User | None:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = body.name
        user.surname = body.surname
        user.email_address = body.email_address
        user.phone_number = body.phone_number
        user.date_of_birth = body.date_of_birth
        user.additional_data = body.additional_data
        db.commit()
    return user


async def update_status_user(user_id: int, body: UsersStatusUpdate, db: Session) -> User | None:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.done = body.done
        db.commit()
    return user
