from sqlalchemy import create_engine, NVARCHAR, Integer, Column, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///db/toDo.db", echo=True)
Base = declarative_base()
session = sessionmaker(bind=engine)()


class ToDo(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True)
    task = Column(NVARCHAR)
    time = Column(DateTime)

    def __init__(self, task=None, time=None):
        self.task = task
        self.time = time


Base.metadata.create_all(engine)