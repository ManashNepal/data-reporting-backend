from config.database import engine, Base 
from app.models.reports import Reports
from app.models.report_columns import Report_Columns
from fastapi import FastAPI
from routes.report_route import router as report_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(report_router)