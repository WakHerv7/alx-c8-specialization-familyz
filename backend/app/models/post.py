from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    content = Column(Text)
    date = Column(Date, nullable=True)

    author_id = Column(Integer, ForeignKey("individual.id"))
    comments = relationship("Comment", backref="post", lazy=True)
    likes = relationship('Like', backref='post', lazy=True)

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
    



