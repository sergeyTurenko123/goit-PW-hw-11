from typing import List, Annotated, Union

from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import UsersBase, UsersStatusUpdate, UsersResponse
from src.repository import users as repository_users


router = APIRouter(prefix='/users')

@router.get("/",  response_model=List[UsersResponse])
async def read_users(skip: int = 0, limit: int = 100, birthdays: int| None=None, db: Session = Depends(get_db)):
    users_birthdays = await repository_users.get_users_birthdays(skip, limit, db)
    users_all = await repository_users.get_users(skip, limit, db)
    if birthdays:
        return users_birthdays
    else:
        return users_all

@router.get("/{user_id}", response_model=UsersResponse)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = await repository_users.get_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.get("/user/", response_model=UsersResponse)
async def read_user(name: str| None=None, surname:  str| None=None, email_address: str| None=None, phone_number: str| None=None, db: Session = Depends(get_db)):
    user = await repository_users.get_user_name(name, surname, email_address, phone_number, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/", response_model=UsersResponse)
async def create_user(body: UsersBase, db: Session = Depends(get_db)):
    return await repository_users.create_user(body, db)


@router.put("/{user_id}", response_model=UsersResponse)
async def update_user(body: UsersBase, user_id: int, db: Session = Depends(get_db)):
    user = await repository_users.update_user(user_id, body, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.patch("/{user_id}", response_model=UsersResponse)
async def update_status_user(body: UsersStatusUpdate, user_id: int, db: Session = Depends(get_db)):
    user = await repository_users.update_status_user(user_id, body, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.delete("/{user_id}", response_model=UsersResponse)
async def remove_user(user_id: int, db: Session = Depends(get_db)):
    user = await repository_users.remove_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
