from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


from db import Base, session


class List(Base):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key=True)
    items = relationship('Item', back_populates='list')

    def __repr__(self):
        return f'List(id={self.id})'

    def save(self):
        session.add(self)
        session.commit()
        return self


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    list_id = Column(Integer, ForeignKey('lists.id'))

    list = relationship('List', back_populates='items')

    def save(self):
        session.add(self)
        session.commit()
        return self

    def __repr__(self):
        return self.content