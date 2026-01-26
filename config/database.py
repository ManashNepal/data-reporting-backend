from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:Betternow10%23@localhost:3306/reportdb"

engine = create_engine(url=DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()