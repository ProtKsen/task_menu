from typing import List

from fastapi import APIRouter, status

from src.db import db_session
from src.models import Dish, Menu, Submenu
from src.repos import DishRepo, MenuRepo, SubmenuRepo
from src.schemas import (DishCreationSchema, DishFullSchema, DishUpdateSchema,
                         MenuCreationSchema, MenuFullSchema, MenuUpdateSchema,
                         SubmenuCreationSchema, SubmenuFullSchema,
                         SubmenuUpdateSchema)

router = APIRouter(prefix='/api/v1')

menu_repo = MenuRepo()
submenu_repo = SubmenuRepo()
dish_repo = DishRepo()


@router.get("/menus/", response_model=List[MenuFullSchema])
def get_all_menus():
    return [menu for menu in Menu.query.all()]


@router.get("/menus/{menu_id}", response_model=MenuFullSchema)
def get_menu_by_id(menu_id: int):
    return menu_repo.get_by_id(menu_id)


@router.post("/menus/", response_model=MenuFullSchema, status_code=status.HTTP_201_CREATED)
def add_menu(menu: MenuCreationSchema):
    new_menu = Menu(title=menu.title, description=menu.description)
    db_session.add(new_menu)
    db_session.commit()
    db_session.refresh(new_menu)
    return new_menu


@router.patch("/menus/{menu_id}", response_model=MenuFullSchema)
def update_menu(menu_id: int, new_menu: MenuUpdateSchema):

    menu = menu_repo.get_by_id(menu_id)

    for attr in dict(new_menu).keys():
        setattr(menu, attr, getattr(new_menu, attr))

    db_session.commit()
    db_session.refresh(menu)
    return menu


@router.delete("/menus/{menu_id}", status_code=status.HTTP_200_OK)
def delete_menu(menu_id: int):
    menu = menu_repo.get_by_id(menu_id)
    db_session.delete(menu)
    db_session.commit()
    return {'id': menu_id}


@router.get("/menus/{menu_id}/submenus", response_model=List[SubmenuFullSchema])
def get_all_submenus(menu_id: int):
    return [submenu for submenu in Submenu.query.filter(Submenu.menu_id == menu_id).all()]


@router.get("/menus/{menu_id}/submenus/{submenu_id}", response_model=SubmenuFullSchema)
def get_submenu_by_id(submenu_id: int):
    submenu = submenu_repo.get_by_id(submenu_id)
    return submenu


@router.post(
    "/menus/{menu_id}/submenus",
    response_model=SubmenuFullSchema,
    status_code=status.HTTP_201_CREATED
)
def add_submenu(menu_id: int, submenu: SubmenuCreationSchema):
    new_submenu = Submenu(title=submenu.title, description=submenu.description, menu_id=menu_id)
    db_session.add(new_submenu)
    db_session.commit()
    db_session.refresh(new_submenu)
    return new_submenu


@router.patch(
    "/menus/{menu_id}/submenus/{submenu_id}",
    response_model=SubmenuFullSchema
)
def update_submenu(submenu_id: int, new_submenu: SubmenuUpdateSchema):

    submenu = submenu_repo.get_by_id(submenu_id)
    for attr in dict(new_submenu).keys():
        setattr(submenu, attr, getattr(new_submenu, attr))

    db_session.commit()
    db_session.refresh(submenu)
    return submenu


@router.delete("/menus/{menu_id}/submenus/{submenu_id}", status_code=status.HTTP_200_OK)
def delete_submenu(submenu_id: int):

    submenu = submenu_repo.get_by_id(submenu_id)

    db_session.delete(submenu)
    db_session.commit()
    return {'id': submenu_id}


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes", response_model=List[DishFullSchema])
def get_all_dishes(submenu_id: int):
    return [dish for dish in Dish.query.filter(Dish.submenu_id == submenu_id).all()]


@router.get(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
    response_model=DishFullSchema
)
def get_dish_by_id(dish_id: int):
    dish = dish_repo.get_by_id(dish_id)
    return dish


@router.post(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes",
    response_model=DishFullSchema,
    status_code=status.HTTP_201_CREATED
)
def add_dish(submenu_id: int, dish: DishCreationSchema):

    new_dish = Dish(
        title=dish.title,
        description=dish.description,
        price=float(dish.price),
        submenu_id=submenu_id
    )
    db_session.add(new_dish)
    db_session.commit()
    db_session.refresh(new_dish)
    return new_dish


@router.patch(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
    response_model=DishFullSchema
)
def update_dish(dish_id: int, new_dish: DishUpdateSchema):
    dish = dish_repo.get_by_id(dish_id)

    for attr in dict(new_dish).keys():
        setattr(dish, attr, getattr(new_dish, attr))

    db_session.commit()
    db_session.refresh(dish)
    return dish


@router.delete(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
    status_code=status.HTTP_200_OK
)
def delete_dish(dish_id: int):
    dish = dish_repo.get_by_id(dish_id)
    db_session.delete(dish)
    db_session.commit()
    return {'id': dish_id}
