from sqlalchemy import Column,Integer,String
from app.database.database import Base
from sqlalchemy.orm import relationship

class Parent(Base):
    __tablename__ = "parents"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    address_street = Column(String)
    address_city = Column(String)
    address_state = Column(String)
    address_zip = Column(String)
    children = relationship("Child", back_populates="parent",lazy='joined')   
    
    
    