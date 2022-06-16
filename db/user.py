from sqlalchemy import *

from db.database import metadata

# user = Table(
#     'user',
#     metadata,
#     Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
#     Column("name", String, index=True, unique=True),
#     Column("email", String, unique=True, primary_key=True),
#     Column("password", String)
# )


fake_db = {
    "johndoe": {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
    },
    "alice": {
        "username": "alice",
        "email": "alice@example.com",
        "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
    },
}
