import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.route import me as me_route

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

app = FastAPI(title="Profile /me API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(me_route.router)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the Profile API. Visit /me for info."}
