from fastapi import FastAPI

from config.database import engine, Base 
from app.models.reports import Reports
from app.models.report_columns import ReportColumn

from routes.report_route import router as report_router
from routes.auth_route import router as auth_router
from routes.query_route import router as query_router
from routes.connection_route import router as connection_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(report_router)
app.include_router(auth_router)
app.include_router(query_router)
app.include_router(connection_router)