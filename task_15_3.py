"""Создать таблицу Школьный дневник(Diary) с помощью sqlalchemy.
Дневник характеризуется Средним баллом и студентом к которому
он привязан.
Получить всех студентов и создать для каждого дневник"""
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey, String

DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'Lesson_15_Diary'
DB_ECHO = True

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    diary = relationship('Diary', back_populates='student')


class Diary(Base):
    __tablename__ = 'diary_student'
    id = Column(Integer, primary_key=True)
    mark = Column(Integer)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', uselist=False, back_populates='diary')



engine = create_engine(
# "postgresql://postgres:postgres@localhost/test",
f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}',
echo=True,
)
if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
diary1 = Diary(mark=8)
student1 = Student(name='Tom', diary = diary1)


session.add_all([student1, diary1])
session.commit()

