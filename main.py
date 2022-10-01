import uvicorn

from fastapi import FastAPI, APIRouter

from core.models.base import Base, engine
from v1.endpoints import user, mail

app = FastAPI()

Base.metadata.create_all(bind=engine)

router_version_1 = APIRouter(prefix='/v1')
router_version_1.include_router(user)
router_version_1.include_router(mail)

app.include_router(router_version_1)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)