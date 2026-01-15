import type { Lot } from "../types/lot";
import { shipLot, updateLot } from "../api/lots";

type Props = {
  lots: Lot[];
  onRefresh: () => void;
};

export function LotTable({ lots, onRefresh }: Props) {
  const handleShip = async (id: number) => {
    try {
      await shipLot(id);
      onRefresh();
    } catch (err: any) {
      alert(err.message);
    }
  };

  const handleQCChange = async (id: number, qc_status: string) => {
    try {
      await updateLot(id, { qc_status });
      onRefresh();
    } catch (err: any) {
      alert(err.message);
    }
  };

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Lot</th>
          <th>QC Status</th>
          <th>Quantity</th>
          <th>Shipped At</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {lots.map((lot) => (
          <tr key={lot.id}>
            <td>{lot.id}</td>
            <td>{lot.lot_number}</td>
            <td>
              <select
                value={lot.qc_status}
                onChange={(e) => handleQCChange(lot.id, e.target.value)}
                disabled={lot.shipped_at !== null || lot.qc_status === "passed"}
              >
                <option value="pending">PENDING</option>
                <option value="passed">PASSED</option>
                <option value="failed">FAILED</option>
              </select>
            </td>
            <td>{lot.quantity}</td>
            <td>{lot.shipped_at ?? "-"}</td>
            <td>
              <button
                className="ship"
                disabled={lot.qc_status !== "passed" || lot.shipped_at !== null}
                onClick={() => handleShip(lot.id)}
              >
                Ship
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}