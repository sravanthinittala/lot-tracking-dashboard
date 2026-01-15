from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.routes import lot_routes, product_routes, warehouse_routes
#from core.logging import logger
from app.models import Lot, Product, Warehouse

# Create tables
Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173", # Vite default port
]

app = FastAPI(title="Lot Traceability API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(lot_routes.router, prefix="/lots", tags=["lots"])
app.include_router(product_routes.router, prefix="/products", tags=["products"])
app.include_router(warehouse_routes.router, prefix="/warehouses", tags=["warehouses"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Lot Traceability API"}