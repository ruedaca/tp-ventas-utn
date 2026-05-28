# SCRUM-2: Script de análisis de ventas - Escenario B
# TP Organización Empresarial - UTN TUP 2026
# Integrantes: Lucas Baccaro y Camila Rueda

import pandas as pd
import matplotlib.pyplot as plt
import os

# Usamos rutas relativas para que funcione en cualquier entorno (Colab, IDE, etc.)
RUTA_DATOS = os.path.join("datos", "ventas.csv")
RUTA_RESULTADOS = "resultados"
os.makedirs(RUTA_RESULTADOS, exist_ok=True)

# --- 1. CARGAR DATOS ---
# parse_dates convierte la columna fecha a tipo datetime automáticamente
df = pd.read_csv(RUTA_DATOS, parse_dates=["fecha"])

# Calculamos el monto por fila para poder sumar ingresos luego
df["monto_total"] = df["cantidad"] * df["precio_unitario"]

# --- 2. INDICADORES GENERALES ---
print(f"Ventas totales: $ {df['monto_total'].sum():,.2f}")
print(f"Unidades vendidas: {df['cantidad'].sum()}")

# --- 3. PRODUCTO MÁS VENDIDO ---
# Agrupamos por producto y sumamos ingresos para saber cuál genera más dinero
por_producto = df.groupby("producto")["monto_total"].sum().sort_values(ascending=False)
print(f"\nProducto con más ingresos: {por_producto.idxmax()}")
print(por_producto)

# --- 4. VENTAS POR MES ---
# Period("M") agrupa por año-mes, evitando mezclar meses de distintos años
df["mes"] = df["fecha"].dt.to_period("M")
por_mes = df.groupby("mes")["monto_total"].sum()
print(f"\nVentas por mes:\n{por_mes}")

# --- 5. GRÁFICO ---
fig, ax = plt.subplots(figsize=(12, 5))
por_mes.plot(kind="bar", ax=ax, color="#4C72B0")
ax.set_title("Evolución de Ventas Mensuales 2024")
ax.set_xlabel("Mes")
ax.set_ylabel("Ingresos ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# Guardamos el gráfico en /resultados
ruta_grafico = os.path.join(RUTA_RESULTADOS, "evolucion_ventas.png")
plt.savefig(ruta_grafico, dpi=150)
plt.show()
print(f"\nGráfico guardado en {ruta_grafico}")