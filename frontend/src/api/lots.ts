const API_BASE = "http://localhost:8000";

export async function fetchLots() {
  const res = await fetch(`${API_BASE}/lots`);
  if (!res.ok) throw new Error("Failed to fetch lots");
  return res.json();
}

export async function shipLot(lotId: number) {
  const res = await fetch(`${API_BASE}/lots/${lotId}/ship`, {
    method: "POST",
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Failed to ship lot");
  }
  return res.json();
}

export async function updateLot(id: number, updates: { qc_status?: string }) {
  const res = await fetch(`${API_BASE}/lots/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(updates),
  });
  if (!res.ok) throw new Error(await res.text());
}