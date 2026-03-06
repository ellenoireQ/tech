"use client";

import { useEffect, useState } from "react";

type SalesItem = {
  product_name: string;
  jumlah_penjualan: number;
  harga: number;
  diskon: number;
  status: string;
};

export default function DashboardPage() {
  const [data, setData] = useState<SalesItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("token");

    fetch("http://127.0.0.1:8000/sales?expand=10", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => {
        if (!res.ok) throw new Error("Failed to retrieve the data.");
        return res.json();
      })
      .then((json) => setData(json.data))
      .catch((err: Error) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="min-h-screen bg-zinc-50 p-8 dark:bg-zinc-950">
      <h1 className="mb-6 text-2xl font-semibold text-zinc-900 dark:text-zinc-50">
        Dashboard Penjualan
      </h1>

      {loading && (
        <p className="text-sm text-zinc-500">Memuat data...</p>
      )}

      {error && (
        <p className="text-sm text-red-500">{error}</p>
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
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
