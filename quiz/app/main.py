from fastapi import FastAPI
from .routers import users, auth, mcq_routes
from .database import engine
from . import models


models.Base.metadata.create_all(bind=engine)  # used to create the db tables if already doesn't exist

app = FastAPI()

# including the routers
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(mcq_routes.router)


@app.get("/")
async def test():
    return {"message": "Hello World"}

