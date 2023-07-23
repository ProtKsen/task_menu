from typing import Optional

from pydantic import BaseModel, field_validator


class IdConverterMixin(BaseModel):
    id: str

    @field_validator('id', mode='before')
    @classmethod
    def convert_int_serial(cls, v):
        if isinstance(v, int):
            v = str(v)
        return v


class MenuCreationSchema(BaseModel):
    title: str
    description: str


class MenuUpdateSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]


class MenuFullSchema(IdConverterMixin, MenuCreationSchema):
    submenus_count: int
    dishes_count: int


class SubmenuCreationSchema(BaseModel):
    title: str
    description: str


class SubmenuUpdateSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]


class SubmenuFullSchema(IdConverterMixin, SubmenuCreationSchema):
    dishes_count: int


class DishCreationSchema(BaseModel):
    title: str
    description: str
    price: str

    @field_validator('price', mode='before')
    @classmethod
    def convert_float_serial(cls, v):
        if isinstance(v, float):
            v = str(round(v, 2))
        return v


class DishUpdateSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[str]


class DishFullSchema(IdConverterMixin, DishCreationSchema):
    pass
