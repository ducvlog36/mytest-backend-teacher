from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta , engine
import datetime as _dt

users = Table('User', meta,
    Column('user_id', Integer, primary_key = True),
    Column('user_email', String(255), unique = True,index=True),
    Column('user_name', String(255)),
    Column('user_hashed_password', String(255)),
    Column('user_type', Integer, default = 2),
    Column('user_type_mota', String(255)),
    Column('createAt', DateTime, default = _dt.datetime.utcnow),
    Column('updateAt', DateTime, default = _dt.datetime.utcnow),
)

meta.create_all(engine)