import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from app.database.connection import get_db
from app.main import app

TEST_DB_URL = "postgresql://testuser:testpass@localhost:5433/test_db"
engine = create_engine(TEST_DB_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SCRIPTS_DIR = "postgres/db_scripts"


def execute_sql_scripts():
    with engine.connect() as conn:
        for filename in sorted(os.listdir(SCRIPTS_DIR)):
            if filename.endswith(".sql"):
                print(f"Executing script: {filename}")
                with open(os.path.join(SCRIPTS_DIR, filename), "r", encoding="utf-8") as f:
                    sql = f.read()
                    conn.execute(text(sql))
        conn.commit()


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    with engine.begin() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE; CREATE SCHEMA public;"))
    execute_sql_scripts()


@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    try:
        yield session
    finally:
        if transaction.is_active:
            transaction.rollback()
        connection.close()


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
