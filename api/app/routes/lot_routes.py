from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.lot_service import LotService
from app.schema.lot import LotCreate, LotUpdate, Lot

router = APIRouter()

@router.post("/", response_model=Lot)
def create_lot(lot: LotCreate, db: Session = Depends(get_db)):
    lot_service = LotService(db)
    return lot_service.create_lot(lot)

@router.get("/{lot_id}", response_model=Lot)
def read_lot(lot_id: int, db: Session = Depends(get_db)):
    lot_service = LotService(db)
    db_lot = lot_service.get_lot(lot_id)
    if db_lot is None:
        raise HTTPException(status_code=404, detail="Lot not found")
    return db_lot

@router.get("/", response_model=list[Lot])
def read_lots(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lot_service = LotService(db)
    return lot_service.get_lots(skip=skip, limit=limit)

@router.patch("/{lot_id}", response_model=Lot)
def update_lot(lot_id: int, lot_update: LotUpdate, db: Session = Depends(get_db)):
    lot_service = LotService(db)
    db_lot = lot_service.update_lot(lot_id, lot_update)
    if db_lot is None:
        raise HTTPException(status_code=404, detail="Lot not found")
    return db_lot

@router.post("/{lot_id}/ship", response_model=Lot)
def ship_lot(lot_id: int, db: Session = Depends(get_db)):
    service = LotService(db)
    return service.ship_lot(lot_id)

@router.delete("/{lot_id}", response_model=dict)
def delete_lot(lot_id: int, db: Session = Depends(get_db)):
    lot_service = LotService(db)
    success = lot_service.delete_lot(lot_id)
    if not success:
        raise HTTPException(status_code=404, detail="Lot not found")
    return {"detail": "Lot deleted successfully"}