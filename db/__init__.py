from .category import category
from .user import user
from .goods import goods
from .basket import basket

from .database import engine, Base

Base.metadata.create_all(engine)
