from os import environ
import databases

DB_USER = environ.get("DB_USER", "dastan")
DB_PASSWORD = environ.get("DB_PASSWORD", "dastan123")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = "todo_db"
DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

database = databases.Database(DATABASE_URL)