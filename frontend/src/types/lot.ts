export type QCStatus = "pending" | "passed" | "failed";

export interface Lot {
  id: number;
  lot_number: string;
  quantity: number;
  qc_status: QCStatus;
  shipped_at: string | null;
}