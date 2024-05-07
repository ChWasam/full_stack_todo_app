from starlette.config import Config
from starlette.datastructures import Secret

# Fastapi connection pattern starlet ka use karta ha 
# Yeh sensitive info ko leak hona sa bachai ga 

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

DATABASE_URL = config("DATABASE_URL", cast=Secret)
