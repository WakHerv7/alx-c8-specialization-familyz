from . import db
from sqlalchemy import inspect
from sqlalchemy import Column, String, Integer, Boolean, inspect

class Entry(db.Model):
    __tablename__ = 'entries'  
    id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String(64), nullable=True)
    description = Column(String(120), nullable=True)
    status = Column(Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }
