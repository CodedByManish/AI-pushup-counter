from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    reps = Column(Integer, nullable=False)
    duration = Column(Float, nullable=False)  # duration in seconds
    form_score = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Session(reps={self.reps}, duration={self.duration}, form_score={self.form_score}, timestamp={self.timestamp})>"