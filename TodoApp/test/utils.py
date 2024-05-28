import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from TodoApp.database import Base
from TodoApp.main import app
from fastapi.testclient import TestClient
import pytest
from TodoApp.models import Todos, Users
from TodoApp.routers.auth import bcrypt_context

# Set up the test database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

# Create an engine and a session for the test database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass = StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the test database
Base.metadata.create_all(bind=engine)

# Override the get_db dependency to use the test database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override the get_current_user dependency to return an authenticated admin user
def override_get_current_user():
    return {'username': 'erchey', 'id': 1, 'role': 'admin'}

# Create a test client
client = TestClient(app)

@pytest.fixture
def test_todo():
    db = TestingSessionLocal()
    todo = Todos(
        title="Learn to code!",
        description="Need to learn everyday!",
        priority=5,
        complete=False,
        owner_id=1,
    )
    db.add(todo)
    db.commit()
    yield todo
    db.query(Todos).delete()
    db.commit()
    db.close()

@pytest.fixture
def test_user():
    db = TestingSessionLocal()
    user = Users(
        username="codingwithrobytest",
        email="codingwithrobytest@email.com",
        first_name="Eric",
        last_name="Roby",
        hashed_password=bcrypt_context.hash("testpassword"),
        role="admin",
        phone_number="(111)-111-1111"
    )
    db.add(user)
    db.commit()
    yield user
    db.query(Users).delete()
    db.commit()
    db.close()
