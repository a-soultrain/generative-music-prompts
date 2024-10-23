from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class ParentGenre(Base):
    __tablename__ = 'parent_genres'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    # Relationships
    main_genres = relationship("MainGenre", backref="parent_genre")
    arrangements = relationship("Arrangement", backref="parent_genre")
    instruments = relationship("Instrument", backref="parent_genre")
    characteristics = relationship("Characteristic", backref="parent_genre")
