from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, DateTime, Integer, DateTime, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.associationproxy import association_proxy


individual_family_association = db.Table(
    "individual_family",
    Column("individual_id", Integer, ForeignKey("individual.id"), primary_key=True),
    Column("family_id", Integer, ForeignKey("family.id"), primary_key=True),
)

class Family(db.Model):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, default=None, onupdate=func.now(), server_default=func.now())
    name = Column(String(255))
    picture_name = Column(String(255), nullable=True)
    picture_path = Column(String(255), nullable=True)

    members = relationship("Individual", secondary=individual_family_association,
                              back_populates="families", lazy="dynamic")
    

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
    



