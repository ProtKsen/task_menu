from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
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
    submenu_id = Column(Integer, ForeignKey("submenus.id"))
    submenu = relationship("Submenu", back_populates="dishes")


class Submenu(Base):
    __tablename__ = "submenus"

    # vital
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    # relations
    dishes = relationship("Dish", back_populates="submenu")
    menu_id = Column(Integer, ForeignKey("menus.id"))
    menu = relationship("Menu", back_populates="submenus")


class Menu(Base):
    __tablename__ = "menus"

    # vital
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    # relations
    submenus = relationship("Submenu", back_populates="menu")
