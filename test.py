from app.services.connection_resolver import resolve_sql_connection
from config.database import get_db 
from sqlalchemy import text

db = next(get_db())

connection_name = "mysql_db"

try:
    engine = resolve_sql_connection(connection_name, db, 2)

    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
finally:
    db.close()

print(result)