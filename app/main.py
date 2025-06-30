# main.py
from fastapi import FastAPI
from app.routes import router
from app.database import create_db
import uvicorn

app = FastAPI(title="Task Management API")

create_db()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)