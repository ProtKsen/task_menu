from pydantic import BaseModel, field_validator
from typing import Optional


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
