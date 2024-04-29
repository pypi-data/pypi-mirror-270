"""app.py"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import database
from models import environment as m_environment
import endpoints.generate_img
import endpoints.pip_compile

app = FastAPI()
# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
# Database setup
db_conn = database.Database()
m_environment.Base.metadata.create_all(bind=db_conn.create_database_engine())

# Routers
app.include_router(endpoints.generate_img.router)
app.include_router(endpoints.pip_compile.router)
