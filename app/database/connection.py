from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.settings import settings

DB_USER = settings.POSTGRES_USER
DB_PASS = settings.POSTGRES_PASSWORD
DB_HOST = settings.POSTGRES_HOST
DB_NAME = settings.POSTGRES_DB
DB_PORT = settings.POSTGRES_PORT

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
