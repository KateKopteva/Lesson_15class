"""Создать таблицу Учебной группы(Group) с помощью
sqlalchemy. Группа характеризуется названием(name)."""

from sqlalchemy import create_engine, String, Table, MetaData, Column, Integer
from sqlalchemy_utils import database_exists, create_database


DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'Lesson_15_1'
DB_ECHO = True
engine = create_engine(
# "postgresql://postgres:postgres@localhost/test",
f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}',
echo=True,
)
if not database_exists(engine.url):

    create_database(engine.url)

meta = MetaData()
group = Table(
    'Group', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)
meta.create_all(engine)