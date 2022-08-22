from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import getenv


def generate_dsn(host, port, username, password, db):
    return f"postgresql://{username}:{password}@{host}:{port}/{db}"


SQLALCHEMY_DATABASE_URL = generate_dsn(
    host=getenv("DB_HOST","localhost"),
    port=getenv("DB_PORT","5432"),
    username=getenv("DB_USER","postgres"),
    password=getenv("DB_PASS","postgres"),
    db=getenv("DB_NAME","db"),
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
