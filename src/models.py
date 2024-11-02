from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)


import database


class Patient(database.Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String, nullable=False)
    lname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    dob = Column(String, nullable=False)
    address = Column(String, nullable=False)
    state = Column(String, nullable=False)
    postal_code = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
