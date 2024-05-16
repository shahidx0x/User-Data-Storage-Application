from sqlalchemy import String,Integer,Column,ForeignKey

from sqlalchemy.orm import relationship
from app.database.database import Base

class Child(Base):
    __tablename__ = "childreen"
    
    id  =Column(Integer,primary_key=True,index=True)
    first_name = Column(String)
    last_name = Column(String)
    parent_id  = Column(Integer,ForeignKey("parents.id"))
    
    parent = relationship("Parents",back_populates="children")
    
    
    
    