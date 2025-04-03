from fastapi import FastAPI
from app.account import router as account_router
from app.brand import router as brand_router
from app.category import router as category_router
from app.size import router as size_router
from app.product import router as product_router
from app.image import router as image_router
from app.inventory import router as inventory_router
from app.customer import router as customer_router
from app.employee import router as employee_router
from app.invoice import router as invoice_router
from app.invoice_details import router as invoice_details_router

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
app.include_router(brand_router.router)
app.include_router(category_router.router)
app.include_router(product_router.router)
app.include_router(image_router.router)
app.include_router(size_router.router)
app.include_router(inventory_router.router)
app.include_router(customer_router.router)
app.include_router(employee_router.router)
app.include_router(invoice_router.router)
app.include_router(invoice_details_router.router)

