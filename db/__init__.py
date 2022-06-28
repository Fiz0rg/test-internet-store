from .category import category
from .user import user
from .goods import goods

from .database import engine, Base

Base.metadata.create_all(engine)
