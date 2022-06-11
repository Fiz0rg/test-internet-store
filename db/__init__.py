from .goods import goods

from .database import metadata, engine

metadata.create_all(engine)
