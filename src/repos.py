from fastapi import HTTPException, status

from src.models import Dish, Menu, Submenu


class BaseRepo():
    name = None
    model = None

    def get_by_id(self, id: int) -> Menu:
        entity = self.model.query.filter(self.model.id == id).first()
        if not entity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.name} not found"
            )
        return entity


class MenuRepo(BaseRepo):
    name = "menu"
    model = Menu


class SubmenuRepo(BaseRepo):
    name = "submenu"
    model = Submenu


class DishRepo(BaseRepo):
    name = "dish"
    model = Dish
