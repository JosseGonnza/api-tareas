import uvicorn
from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="API de tareas")
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
