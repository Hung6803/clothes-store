from fastapi import FastAPI
from app.account import router as account_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Clothes Store")

origins = [
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(account_router.router)


