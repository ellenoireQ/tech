"use client";

import { useEffect, useState } from "react";

type SalesItem = {
  product_name: string;
  jumlah_penjualan: number;
  harga: number;
  diskon: number;
  status: string;
};

const EXPAND_OPTIONS = [5, 10, 25, 50, 100];

export default function DashboardPage() {
  const [data, setData] = useState<SalesItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [expand, setExpand] = useState(10);
  const [predictions, setPredictions] = useState<string[]>([]);
  const [predicting, setPredicting] = useState(false);
  const [predictError, setPredictError] = useState("");

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/sales?expand=${expand}`, {
      credentials: "include",
    })
      .then((res) => {
        if (!res.ok) throw new Error("Failed to retrieve the data.");
        return res.json();
      })
      .then((json) => {
        setData(json.data);
        setPredictions([]);
      })
      .catch((err: Error) => setError(err.message))
      .finally(() => setLoading(false));
  }, [expand]);

  const handlePredict = async () => {
    setPredicting(true);
    setPredictError("");
    try {
      const res = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify({ data }),
      });
      if (!res.ok) throw new Error("Prediction failed.");
      const json = await res.json();
      setPredictions(json.predictions);
    } catch (err: unknown) {
      if (err instanceof Error) setPredictError(err.message);
    } finally {
      setPredicting(false);
    }
  };

  return (
    <div className="min-h-screen bg-zinc-50 p-8 dark:bg-zinc-950">
      <div className="mb-6 flex items-center justify-between">
        <h1 className="text-2xl font-semibold text-zinc-900 dark:text-zinc-50">
          Dashboard Penjualan
        </h1>
        <div className="flex items-center gap-2">
          <label className="text-sm text-zinc-500 dark:text-zinc-400">Tampilkan</label>
          <select
            value={expand}
            onChange={(e) => {
              setLoading(true);
              setExpand(Number(e.target.value));
            }}
            className="rounded-lg border border-zinc-300 bg-white px-3 py-1.5 text-sm text-zinc-900 outline-none transition focus:border-zinc-600 dark:border-zinc-700 dark:bg-zinc-800 dark:text-zinc-50 dark:focus:border-zinc-400"
          >
            {EXPAND_OPTIONS.map((opt) => (
              <option key={opt} value={opt}>
                {opt}
              </option>
            ))}
          </select>
          <button
            onClick={handlePredict}
            disabled={predicting || loading || data.length === 0}
            className="rounded-lg bg-zinc-900 px-4 py-1.5 text-sm font-medium text-white transition hover:bg-zinc-700 disabled:opacity-50 dark:bg-zinc-50 dark:text-zinc-900 dark:hover:bg-zinc-200"
          >
            {predicting ? "Memproses..." : "Prediksi"}
          </button>
        </div>
      </div>

      {loading && (
        <p className="text-sm text-zinc-500">Memuat data...</p>
      )}

      {error && (
        <p className="text-sm text-red-500">{error}</p>
      )}

      {predictError && (
        <p className="text-sm text-red-500">{predictError}</p>
      )}

      {!loading && !error && (
        <div className="overflow-x-auto rounded-xl border border-zinc-200 dark:border-zinc-800">
          <table className="w-full text-sm text-left text-zinc-700 dark:text-zinc-300">
            <thead className="bg-zinc-100 text-xs uppercase text-zinc-500 dark:bg-zinc-800 dark:text-zinc-400">
              <tr>
                <th className="px-4 py-3">Produk</th>
                <th className="px-4 py-3">Jumlah Penjualan</th>
                <th className="px-4 py-3">Harga</th>
                <th className="px-4 py-3">Diskon (%)</th>
                <th className="px-4 py-3">Status</th>
                {predictions.length > 0 && (
                  <th className="px-4 py-3">Prediksi</th>
                )}
              </tr>
            </thead>
            <tbody>
              {data.map((item, i) => (
                <tr
                  key={i}
                  className="border-t border-zinc-200 bg-white hover:bg-zinc-50 dark:border-zinc-800 dark:bg-zinc-900 dark:hover:bg-zinc-800"
                >
                  <td className="px-4 py-3 font-medium text-zinc-900 dark:text-zinc-50">
                    {item.product_name}
                  </td>
                  <td className="px-4 py-3">{item.jumlah_penjualan}</td>
                  <td className="px-4 py-3">
                    Rp {item.harga.toLocaleString("id-ID")}
                  </td>
                  <td className="px-4 py-3">{item.diskon}%</td>
                  <td className="px-4 py-3">
                    <span
                      className={`rounded-full px-2 py-0.5 text-xs font-medium ${
                        item.status === "Laris"
                          ? "bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300"
                          : "bg-red-100 text-red-600 dark:bg-red-900 dark:text-red-300"
                      }`}
                    >
                      {item.status}
                    </span>
                  </td>
                  {predictions.length > 0 && (
                    <td className="px-4 py-3">
                      <span
                        className={`rounded-full px-2 py-0.5 text-xs font-medium ${
                          predictions[i] === "Laris"
                            ? "bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300"
                            : "bg-orange-100 text-orange-600 dark:bg-orange-900 dark:text-orange-300"
                        }`}
                      >
                        {predictions[i]}
                      </span>
                    </td>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
