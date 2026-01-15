import { useEffect, useState } from "react";
import { fetchLots } from "./api/lots";
import { LotTable } from "./components/LotTable";
import type { Lot } from "./types/lot";
//import './App.css';

function App() {
  const [lots, setLots] = useState<Lot[]>([]);

  const loadLots = async () => {
    try {
      const data = await fetchLots();
      setLots(data);
    } catch (err) {
      alert("Failed to load lots");
    }
  };

  useEffect(() => {
    loadLots();
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Lot Traceability Dashboard</h1>
      <LotTable lots={lots} onRefresh={loadLots} />
    </div>
  );
}

export default App;
