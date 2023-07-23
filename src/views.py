from typing import List

from fastapi import APIRouter, HTTPException, status

from src.db import db_session
from src.models import Menu
from src.schemas import MenuCreationSchema, MenuUpdateSchema, MenuFullSchema

router = APIRouter(prefix='/api/v1')


@router.get("/menus/", response_model=List[MenuFullSchema])
def get_all_menus():
    return [menu for menu in Menu.query.all()]


@router.get("/menus/{menu_id}", response_model=MenuFullSchema)
def get_menu_by_id(menu_id: int):
    menu = Menu.query.filter(Menu.id == menu_id).first()
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="menu not found")
    return menu


@router.post("/menus/", response_model=MenuFullSchema, status_code=status.HTTP_201_CREATED)
def add_menu(menu: MenuCreationSchema):
    new_menu = Menu(title=menu.title, description=menu.description)
    db_session.add(new_menu)
    db_session.commit()
    db_session.refresh(new_menu)
    return new_menu


@router.patch("/menus/{menu_id}", response_model=MenuFullSchema)
def update_menu(menu_id: int, new_menu: MenuUpdateSchema):
    menu = Menu.query.filter(Menu.id == menu_id).first()
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="menu not found")

    for attr in dict(new_menu).keys():
        setattr(menu, attr, getattr(new_menu, attr))

    db_session.commit()
    db_session.refresh(menu)
    return menu


@router.delete("/menus/{menu_id}", status_code=status.HTTP_200_OK)
def delete_menu(menu_id: int):
    menu = Menu.query.filter(Menu.id == menu_id).first()
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="menu not found")
    db_session.delete(menu)
    db_session.commit()
    return {'id': menu_id}
