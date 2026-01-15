# # test_service.py
# import sys
# import os

# # Add project root to Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from app.core.database import SessionLocal, Base, engine
from app.services.lot_service import LotService
from app.services.product_service import ProductService
from app.services.warehouse_service import WarehouseService
from app.schema.lot import LotCreate
from app.schema.product import ProductCreate
from app.schema.warehouse import WarehouseCreate
from app.models.qc_status_enum import QCStatusEnum as QCStatus
from app.models import Lot, Product, Warehouse

Base.metadata.create_all(bind=engine)

db = SessionLocal()
lot_service = LotService(db)
product_service = ProductService(db)
warehouse_service = WarehouseService(db)


new_product = ProductCreate(
    name="Test Product",
    description="A product for testing",
    price=9.99
)

new_warehouse = WarehouseCreate(
    name="Test Warehouse",
    location="123 Test St",
    capacity=1000
)

prod = product_service.create_product(new_product)
print(f"Created product: id={prod.id}, name={prod.name}, price={prod.price}")
warehouse = warehouse_service.create_warehouse(new_warehouse)
print(f"Created warehouse: id={warehouse.id}, name={warehouse.name}, location={warehouse.location}")


# Create a new lot
new_lot = LotCreate(
    lot_number="LOT003",
    product_id=1,
    warehouse_id=1,
    quantity=75,
    qc_status=QCStatus.PENDING
)
lot = lot_service.create_lot(new_lot)
print(f"Created lot: id={lot.id}, lot_number={lot.lot_number}, quantity={lot.quantity}, qc_status={lot.qc_status}")

# List all lots
lots = lot_service.get_lots()
for l in lots:
    print(f"id={l.id}, lot_number={l.lot_number}, quantity={l.quantity}, qc_status={l.qc_status}")

db.close()

