from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from db.database import database
from apps.routes import routes



app = FastAPI(
    title='Todo App',
    description='Author Dastan Alymbek uulu',
    version='1.0'
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(routes)

