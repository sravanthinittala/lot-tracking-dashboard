from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base
from app.models.qc_status_enum import QCStatusEnum

class Lot(Base):
    __tablename__ = "lots"

    id = Column(Integer, primary_key=True, index=True)
    lot_number = Column(String, unique=True, index=True, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    qc_status = Column(Enum(QCStatusEnum), default="pending", nullable=False)

    shipped_at = Column(DateTime, nullable=True)

    product = relationship("Product", back_populates="lots")
    warehouse = relationship("Warehouse", back_populates="lots")