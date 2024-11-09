from app2.backend.db import Base
from sqlalchemy import Integer, String, ForeignKey, Boolean, Column
from sqlalchemy.orm import relationship
from app2.models.task import Task


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='user')


from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))



