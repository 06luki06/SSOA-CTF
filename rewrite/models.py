from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'employees'  # Matches 'nuclear.employees'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    password = Column(String, nullable=False)

    comments_written = relationship('Comment', back_populates='author', foreign_keys='Comment.author_id')
    comments_received = relationship('Comment', back_populates='recipient', foreign_keys='Comment.recipient_id')

class Comment(Base):
    __tablename__ = 'comments'  # Matches 'nuclear.comments'

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    recipient_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    comment = Column(String, nullable=False)

    author = relationship('User', back_populates='comments_written', foreign_keys=[author_id])
    recipient = relationship('User', back_populates='comments_received', foreign_keys=[recipient_id])
