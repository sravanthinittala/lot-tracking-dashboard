from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from app.models.qc_status_enum import QCStatusEnum as QCStatus
from app.models.lot import Lot
from app.schema.lot import LotCreate, LotUpdate

class LotService:
    def __init__(self, db: Session):
        self.db = db

    def create_lot(self, lot_data: LotCreate) -> Lot:
        lot_dict = lot_data.model_dump()
        new_lot = Lot(**lot_dict)
        self.db.add(new_lot)
        self.db.commit()
        self.db.refresh(new_lot)
        return new_lot
    
    def get_lots(self, skip: int = 0, limit: int = 100) -> list[Lot]:
        return self.db.query(Lot).offset(skip).limit(limit).all()

    def get_lot(self, lot_id: int) -> Lot | None:
        return self.db.query(Lot).filter(Lot.id == lot_id).first()

    def ship_lot(self, lot_id: int) -> Lot:
        lot = self.db.query(Lot).filter(Lot.id == lot_id).first()

        if not lot:
            raise HTTPException(status_code=404, detail="Lot not found")

        if lot.shipped_at is not None:
            raise HTTPException(status_code=400, detail="Lot already shipped")

        if lot.qc_status != QCStatus.PASSED:
            raise HTTPException(
                status_code=400,
                detail="Lot cannot be shipped until QC has PASSED"
            )
        
        if lot.quantity <= 0:
            raise HTTPException(
                status_code=400,
                detail="Lot cannot be shipped with zero or negative quantity"
            )

        lot.shipped_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(lot)
        return lot

    def update_lot(self, lot_id: int, lot_update: LotUpdate) -> Lot | None:
        lot = self.get_lot(lot_id)
        if not lot:
            return None
        if lot_update.quantity is not None:
            lot.quantity = lot_update.quantity
        if lot_update.qc_status is not None:
            lot.qc_status = lot_update.qc_status
        self.db.commit()
        self.db.refresh(lot)
        return lot

    def delete_lot(self, lot_id: int) -> bool:
        lot = self.get_lot(lot_id)
        if not lot:
            return False
        self.db.delete(lot)
        self.db.commit()
        return True