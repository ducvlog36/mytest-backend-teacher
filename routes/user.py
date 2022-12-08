from fastapi import APIRouter
from schemas.user import User
from models.user import users
from config.db import conn

user = APIRouter()

@user.get('/')
async def fetch_users():
    return conn.execute(users.select()).fetchall()

@user.get('/{id}')
async def fetch_user(id:int):
    return conn.execute(users.select().where(users.c.user_id == id)).first()

@user.post('/')
async def create_user(user : User):
    listUser = conn.execute(users.select()).fetchall()
    for u in listUser:
        if u.user_email == user.email:
            return "email da ton tai"
    conn.execute(users.insert().values(
        user_name = user.name,
        user_email = user.email,
        user_hashed_password = user.password,
    ))
    return conn.execute(users.select()).fetchall()


@user.put('/{id}')
async def update_user(id: int, user: User):
    conn.execute(users.update().values(
        user_name = user.name,
        user_hashed_password = user.password,
    ).where(users.c.user_id == id))
    return conn.execute(users.select()).fetchall()

@user.delete('/{id}')
async def delete_user(id: int):
    conn.execute(users.delete().where(users.c.user_id == id))
    return conn.execute(users.select()).fetchall()


@user.post('/login')
async def user_login(user : User):
    listUser = conn.execute(users.select()).fetchall()
    for u in listUser:
        if u.user_email == user.email and u.user_hashed_password == user.password: 
            return conn.execute(users.select().where(users.c.user_id == u.user_id)).first()
        else :
            return "Tài khoản hoặc mật khẩu không trùng khớp"
