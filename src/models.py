from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from src.db import Base


class Dish(Base):
    __tablename__ = "dishes"

    # vital
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Numeric(scale=2), nullable=False)

    # relations
    submenu_id = Column(Integer, ForeignKey("submenus.id", ondelete="CASCADE"))
    submenu = relationship("Submenu", back_populates="dishes")


class Submenu(Base):
    __tablename__ = "submenus"

    # vital
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    # relations
    dishes = relationship("Dish", cascade='all,delete', back_populates="submenu")
    _dishes_count = Column(Integer)

    @hybrid_property
    def dishes_count(self):
        return len(self.dishes)

    menu_id = Column(Integer, ForeignKey("menus.id", ondelete="CASCADE"))
    menu = relationship("Menu", back_populates="submenus")


class Menu(Base):
    __tablename__ = "menus"

    # vital
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    # relations
    submenus = relationship("Submenu", cascade='all,delete', back_populates="menu")
    _submenus_count = Column(Integer)

    @hybrid_property
    def submenus_count(self):
        return len(self.submenus)

    _dishes_count = Column(Integer)

    @hybrid_property
    def dishes_count(self):
        return sum([submenu.dishes_count for submenu in self.submenus])
