from app.controllers.parent_controller import (
    create
)
from app.models.parent_model import Parent
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

def create_test_session():
    try:
        engine = create_engine("sqlite:///:memory:") 
        Base = declarative_base()
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        yield db
    finally:
        db.close()
        engine.dispose()

def test_create_parent():
    with create_test_session() as db:
        data = {"first_name": "John", "last_name": "Doe", "address_city": "Anytown",
                "address_zip": "12345", "address_street": "123 Main St", "address_state": "CA"}
        parent = create(db, data)
        assert isinstance(parent, Parent)
        assert parent.first_name == data["first_name"]
        assert parent.last_name == data["last_name"]
        assert parent.address_city == data["address_city"]
        assert parent.address_state == data["address_state"]
        assert parent.address_street == data["address_street"]
        assert parent.address_zip == data["address.zip"]