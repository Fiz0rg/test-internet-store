from pydantic import BaseModel


class CategorySchemas(BaseModel):
    """ Схема проверки категорий. """

    name: str


class CategorySchemasId(CategorySchemas):
    id: int
