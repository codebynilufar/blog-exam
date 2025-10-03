from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    host=Config.DB_HOST,
    port=Config.DB_PORT,
    username=Config.DB_USER,
    password=Config.DB_PASSWORD,
    database=Config.DB_NAME,
)


engine = create_engine(DATABASE_URL)
LocalSession = sessionmaker(bind=engine)
Base = declarative_base()


def initial_db():
    from models import User, Post, Comment 
    Base.metadata.create_all(engine)

   
