from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy


class Like(db.Model):
    id = Column(Integer, primary_key=True)

    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    liked_by_id = Column(Integer, ForeignKey('individual.id'), nullable=False)
    

    # @property
    def save(self):
        db.session.add(self)
        db.session.commit()

    # @classmethod
    def set_members(self, member_list):
        self.members = member_list
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
    



