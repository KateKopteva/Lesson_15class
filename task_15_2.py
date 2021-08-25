'''
Создать таблицу Студент(Student) с помощью sqlalchemy. Студент
характеризуется именем(firstname) и фамилией (lastname) и группой к которой
он приурочен. Создать две группы. Добавить в каждую по три студента
'''
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, backref
from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey, String

DB_USER='test'
DB_PASSWORD='test'
DB_NAME='test'
DB_ECHO = True

Base = declarative_base()

class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship('Group', back_populates='students')

Group.students = relationship('Student', order_by=Student.id, back_populates = 'group')

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}')
if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
group1 = Group(name='Luckies')
student1 = Student(firstname='Ivan', lastname='Petrov', group=group1)
student2 = Student(firstname='Petr', lastname='Ivanov', group=group1)

group2 = Group(name='Loosers')
student3 = Student(firstname='John', lastname='Doe', group=group2)
student4 = Student(firstname='Jane', lastname='Doe', group=group2)
student5 = Student(firstname='Test', lastname='Check', group=group2)

session.add_all([group1, group2, student1, student2, student3, student4, student5])
session.commit()