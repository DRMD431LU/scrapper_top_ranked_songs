from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Song(Base):
    __tablename__ = "song"

    key_id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    position = Column(Integer)

def create_db():
    engine = create_engine('sqlite:///songs.sqlite3')
    Base.metadata.create_all(engine)

def create_session():
    engine = create_engine('sqlite:///songs.sqlite3')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session