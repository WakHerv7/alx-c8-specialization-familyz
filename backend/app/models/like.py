from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, DateTime, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.associationproxy import association_proxy


class Like(db.Model):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, default=None, onupdate=func.now(), server_default=func.now())

    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    liked_by_id = Column(Integer, ForeignKey('individual.id'), nullable=False)
    

    # @property
    def save(self):
        db.session.add(self)
        db.session.commit()

    # @classmethod
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    # @classmethod
    def to_dict(self):
        result = self.__dict__.copy()
        result.pop('_sa_instance_state', None)
        return result
    
    @classmethod
    def find_by_post_id(cls, id):
        response = db.session.query(cls).filter(cls.post_id == id).all()
        # return [] if response == None else response
        return response
        



