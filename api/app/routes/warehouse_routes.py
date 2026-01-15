from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.core.database import get_db
from app.services.warehouse_service import WarehouseService
from app.schema.warehouse import WarehouseCreate, WarehouseUpdate, Warehouse

router = APIRouter()

@router.post("/", response_model=Warehouse)
def create_warehouse(warehouse: WarehouseCreate, db: Session = Depends(get_db)):
    warehouse_service = WarehouseService(db)
    return warehouse_service.create_warehouse(warehouse)

@router.get("/{warehouse_id}", response_model=Warehouse)
def read_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    warehouse_service = WarehouseService(db)
    db_warehouse = warehouse_service.get_warehouse(warehouse_id)
    if db_warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return db_warehouse

@router.get("/", response_model=list[Warehouse])
def read_warehouses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    warehouse_service = WarehouseService(db)
    return warehouse_service.get_warehouses(skip=skip, limit=limit)

@router.patch("/{warehouse_id}", response_model=Warehouse)
def update_warehouse(warehouse_id: int, warehouse_update: WarehouseUpdate, db: Session = Depends(get_db)):
    warehouse_service = WarehouseService(db)
    db_warehouse = warehouse_service.update_warehouse(warehouse_id, warehouse_update)
    if db_warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return db_warehouse

@router.delete("/{warehouse_id}", response_model=dict)
def delete_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    warehouse_service = WarehouseService(db)
    success = warehouse_service.delete_warehouse(warehouse_id)
    if not success:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return {"detail": "Warehouse deleted successfully"}