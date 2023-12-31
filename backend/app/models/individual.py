from . import db
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

from sqlalchemy import Column, Text, DateTime, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.associationproxy import association_proxy
from app.models.family import individual_family_association

spouse_association = db.Table('spouse_association',
    Column('individual_id', Integer, ForeignKey('individual.id')),
    Column('spouse_id', Integer, ForeignKey('individual.id'))
)

class Individual(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, default=None, onupdate=func.now(), server_default=func.now())
    name = Column(String(255))
    username = Column(String(255))
    password = Column(String(100), nullable=True)
    gender = Column(String(5))
    generation = Column(Integer, nullable=True)
    parent_male_id = Column(Integer, nullable=True)
    parent_female_id = Column(Integer, nullable=True)
    birth_rank = Column(Integer, nullable=True)
    dead = Column(Boolean, default=False)
    youngdead = Column(Boolean, default=False)
    birth_date = Column(Date, nullable=True)
    birth_place = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    telephone = Column(String(255), nullable=True)
    profession = Column(String(255), nullable=True)
    country = Column(String(255), nullable=True)
    city = Column(String(255), nullable=True)
    linkedin = Column(String(255), nullable=True)
    twitter = Column(String(255), nullable=True)
    facebook = Column(String(255), nullable=True)
    instagram = Column(String(255), nullable=True)
    aboutme = Column(Text, nullable=True)
    isIncomingSpouse = Column(Boolean, default=False)
    sFatherName = Column(String(255), nullable=True)
    sFatherDead = Column(Boolean, default=False)
    sMotherName = Column(String(255), nullable=True)
    sMotherDead = Column(Boolean, default=False)
    photoName = Column(String(255), nullable=True)
    # You'll need Flask-Uploads or similar package to handle file uploads
    photoPath = Column(String(255), nullable=True)
    photoPath = Column(Boolean, nullable=True)
    is_ghost = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)

    spouses = relationship("Individual", secondary=spouse_association,
                           primaryjoin=id == spouse_association.c.individual_id,
                           secondaryjoin=id == spouse_association.c.spouse_id,
                           backref="related_spouses")

    families = relationship("Family", secondary=individual_family_association,
                               lazy="dynamic", back_populates="members", overlaps="family,members")

    # posts = relationship("Post", backref="author", lazy=True)
    # comments = relationship("Comment", backref="author", lazy=True)
    # likes = relationship('Like', backref='liked_by', lazy=True)



    # @property
    def save(self):
        db.session.add(self)
        db.session.commit()

    # @classmethod
    def set_spouses(self, spouse_list):
        self.spouses = spouse_list
        for spouse in spouse_list:
            if self not in spouse.spouses:
                spouse.spouses.append(self)
        db.session.commit()
    
    def set_families(self, family_list):
        self.families = family_list
        db.session.commit()

    # @classmethod
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def spouseslist(self):
        return self.spouses

    
    # @classmethod
    def to_dict(self):
        result = self.__dict__.copy()
        result.pop('_sa_instance_state', None)
        return result
    
    def __eq__(self, other):
        if isinstance(other, Individual):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
    



