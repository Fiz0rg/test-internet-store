from .goods import goods
from .category import category
from .user import user

from .database import metadata, engine

metadata.create_all(engine)
