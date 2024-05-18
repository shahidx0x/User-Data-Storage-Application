from sqlalchemy import String,Integer,Column,ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Child(Base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    parent_id = Column(Integer, ForeignKey("parents.id"))
    parent = relationship("Parent", back_populates="children",lazy='joined')
    

    
    