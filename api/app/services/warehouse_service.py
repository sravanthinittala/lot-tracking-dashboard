from sqlalchemy.orm import Session
from app.models.warehouse import Warehouse
from app.schema.warehouse import WarehouseCreate, WarehouseUpdate

class WarehouseService:
    def __init__(self, db: Session):
        self.db = db

    def create_warehouse(self, warehouse_data: WarehouseCreate) -> Warehouse:
        warehouse_dict = warehouse_data.model_dump()
        new_warehouse = Warehouse(**warehouse_dict)
        self.db.add(new_warehouse)
        self.db.commit()
        self.db.refresh(new_warehouse)
        return new_warehouse
    
    def get_warehouses(self, skip: int = 0, limit: int = 100) -> list[Warehouse]:
        return self.db.query(Warehouse).offset(skip).limit(limit).all()

    def get_warehouse(self, warehouse_id: int) -> Warehouse | None:
        return self.db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()

    def update_warehouse(self, warehouse_id: int, warehouse_update: WarehouseUpdate) -> Warehouse | None:
        warehouse = self.get_warehouse(warehouse_id)
        if not warehouse:
            return None
        if warehouse_update.name is not None:
            warehouse.name = warehouse_update.name
        if warehouse_update.location is not None:
            warehouse.location = warehouse_update.location
        if warehouse_update.capacity is not None:
            warehouse.capacity = warehouse_update.capacity
        self.db.commit()
        self.db.refresh(warehouse)
        return warehouse

    def delete_warehouse(self, warehouse_id: int) -> bool:
        warehouse = self.get_warehouse(warehouse_id)
        if not warehouse:
            return False
        self.db.delete(warehouse)
        self.db.commit()
        return True