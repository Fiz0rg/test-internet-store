from .goods import goods
from .category import category

from .database import metadata, engine

metadata.create_all(engine)
