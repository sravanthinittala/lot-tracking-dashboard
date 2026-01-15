from pydantic import BaseModel
from app.models.qc_status_enum import QCStatusEnum
from datetime import datetime

class LotBase(BaseModel):
    lot_number: str
    product_id: int
    quantity: int
    warehouse_id: int
    qc_status: QCStatusEnum = QCStatusEnum.PENDING
    shipped_at: datetime | None

class LotCreate(LotBase):
    pass

class LotUpdate(BaseModel):
    quantity: int | None = None
    qc_status: QCStatusEnum | None = None

class Lot(LotBase):
    id: int

    class Config:
        orm_mode = True