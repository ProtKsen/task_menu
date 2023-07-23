from typing import List

from fastapi import APIRouter, HTTPException, status

from src.db import db_session
from src.models import Menu, Submenu
from src.schemas import (MenuCreationSchema, MenuUpdateSchema, MenuFullSchema,
                         SubmenuCreationSchema, SubmenuUpdateSchema, SubmenuFullSchema)

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


@router.get("/menus/{menu_id}/submenus", response_model=List[SubmenuFullSchema])
def get_all_submenus(menu_id: int):
    return [submenu for submenu in Submenu.query.filter(Submenu.menu_id == menu_id).all()]


@router.get("/menus/{menu_id}/submenus/{submenu_id}", response_model=SubmenuFullSchema)
def get_submenu_by_id(submenu_id: int):
    submenu = Submenu.query.filter(Submenu.id == submenu_id).first()
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="submenu not found")
    return submenu


@router.post("/menus/{menu_id}/submenus", response_model=SubmenuFullSchema, status_code=status.HTTP_201_CREATED)
def add_submenu(menu_id: int, submenu: SubmenuCreationSchema):
    new_submenu = Submenu(title=submenu.title, description=submenu.description, menu_id=menu_id)
    db_session.add(new_submenu)
    db_session.commit()
    db_session.refresh(new_submenu)
    return new_submenu


@router.patch("/menus/{menu_id}/submenus/{submenu_id}", response_model=SubmenuFullSchema)
def update_submenu(submenu_id: int, new_submenu: SubmenuUpdateSchema):
    submenu = Submenu.query.filter(Submenu.id == submenu_id).first()
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="submenu not found")

    for attr in dict(new_submenu).keys():
        setattr(submenu, attr, getattr(new_submenu, attr))

    db_session.commit()
    db_session.refresh(submenu)
    return submenu


@router.delete("/menus/{menu_id}/submenus/{submenu_id}", status_code=status.HTTP_200_OK)
def delete_submenu(submenu_id: int):
    submenu = Submenu.query.filter(Submenu.id == submenu_id).first()
    if not submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="submenu not found")
    db_session.delete(submenu)
    db_session.commit()
    return {'id': submenu_id}
