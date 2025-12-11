from pathlib import Path
import pandas as pd
import json

# -------------------------------------------------
# 1. Rutas base
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]  # carpeta p09_dashboard_html
DATA_PATH = BASE_DIR / "data" / "kpis_operacion_demo.csv"
DIST_DIR = BASE_DIR / "dist"
DIST_DIR.mkdir(exist_ok=True)
OUTPUT_HTML = DIST_DIR / "dashboard_p09.html"

print(f"📂 Leyendo datos desde: {DATA_PATH}")

# -------------------------------------------------
# 2. Cargar dataset
# -------------------------------------------------
df = pd.read_csv(DATA_PATH)

# Esperamos columnas:
# mes, disponibilidad_operacional_pct, backlog_ordenes_trabajo, tickets_resueltos_sla_pct
expected_cols = {
    "mes",
    "disponibilidad_operacional_pct",
    "backlog_ordenes_trabajo",
    "tickets_resueltos_sla_pct",
}

missing = expected_cols - set(df.columns)
if missing:
    raise ValueError(f"Faltan columnas en el CSV: {missing}")

# -------------------------------------------------
# 3. Extraer KPIs del último mes
# -------------------------------------------------
last_row = df.iloc[-1]

kpi_disp = float(last_row["disponibilidad_operacional_pct"])
kpi_backlog = int(last_row["backlog_ordenes_trabajo"])
kpi_sla = float(last_row["tickets_resueltos_sla_pct"])
kpi_mes = str(last_row["mes"])

# -------------------------------------------------
# 4. Preparar datos para gráficos
# -------------------------------------------------
labels = df["mes"].tolist()
disp_series = df["disponibilidad_operacional_pct"].tolist()
backlog_series = df["backlog_ordenes_trabajo"].tolist()
sla_series = df["tickets_resueltos_sla_pct"].tolist()

labels_js = json.dumps(labels, ensure_ascii=False)
disp_js = json.dumps(disp_series)
backlog_js = json.dumps(backlog_series)
sla_js = json.dumps(sla_series)

# -------------------------------------------------
# 5. Plantilla HTML simple + Chart.js
# -------------------------------------------------
html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>Dashboard Operacional – Hugo Baghetti</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    :root {{
      --bg: #050816;
      --card-bg: #0b1220;
      --accent: #facc15;
      --accent-soft: rgba(250, 204, 21, 0.15);
      --text: #e5e7eb;
      --muted: #9ca3af;
      --border: #1f2937;
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "SF Pro Text",
        "Segoe UI", sans-serif;
      background: radial-gradient(circle at top, #111827, #020617 55%, #000 100%);
      color: var(--text);
    }}
    .page {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 24px 20px 40px;
    }}
    header {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 24px;
      border-bottom: 1px solid rgba(148, 163, 184, 0.2);
      padding-bottom: 16px;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(15, 23, 42, 0.8);
      border-radius: 999px;
      padding: 4px 12px;
      font-size: 12px;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}
    .badge-dot {{
      width: 6px;
      height: 6px;
      border-radius: 999px;
      background: #22c55e;
      box-shadow: 0 0 0 6px rgba(34, 197, 94, 0.25);
    }}
    h1 {{
      font-size: 26px;
      margin: 0;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
    }}
    h1 span.accent {{
      color: var(--accent);
    }}
    .subtitle {{
      font-size: 14px;
      color: var(--muted);
      max-width: 720px;
    }}
    .grid-kpi {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin: 24px 0 28px;
    }}
    .card {{
      background: radial-gradient(circle at top left, var(--accent-soft), var(--card-bg));
      border-radius: 18px;
      border: 1px solid rgba(148, 163, 184, 0.25);
      padding: 16px 16px 14px;
      box-shadow: 0 18px 40px rgba(15, 23, 42, 0.9);
    }}
    .card small {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--muted);
    }}
    .card-value {{
      font-size: 26px;
      font-weight: 600;
      margin-top: 6px;
      display: flex;
      align-items: baseline;
      gap: 4px;
    }}
    .card-value span.unit {{
      font-size: 13px;
      color: var(--muted);
      font-weight: 400;
    }}
    .card-footnote {{
      margin-top: 8px;
      font-size: 12px;
      color: var(--muted);
    }}
    .layout-charts {{
      display: grid;
      grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr);
      gap: 18px;
    }}
    @media (max-width: 900px) {{
      .layout-charts {{
        grid-template-columns: minmax(0, 1fr);
      }}
    }}
    .chart-card {{
      background: radial-gradient(circle at top, rgba(15, 23, 42, 0.7), #020617);
      border-radius: 18px;
      border: 1px solid var(--border);
      padding: 16px 16px 18px;
    }}
    .chart-header {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      gap: 10px;
      margin-bottom: 10px;
    }}
    .chart-header h2 {{
      font-size: 15px;
      margin: 0;
    }}
    .chart-header span {{
      font-size: 12px;
      color: var(--muted);
    }}
    footer {{
      margin-top: 28px;
      font-size: 11px;
      color: var(--muted);
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
      border-top: 1px dashed rgba(148, 163, 184, 0.3);
      padding-top: 10px;
    }}
    footer a {{
      color: var(--accent);
      text-decoration: none;
    }}
    footer a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <div class="page">
    <header>
      <div class="badge">
        <span class="badge-dot"></span>
        Operational Analytics · Executive View
      </div>
      <h1>
        Operational KPIs Dashboard
        <span class="accent">· Último mes: {kpi_mes}</span>
      </h1>
      <p class="subtitle">
        Resumen ejecutivo de desempeño operacional a partir de un dataset de ejemplo
        con indicadores de disponibilidad, backlog de mantenimiento y cumplimiento de
        SLA en tickets de soporte. Diseñado como pieza de portafolio técnico por
        Hugo Baghetti (analytics-tech-portfolio).
      </p>
    </header>

    <section class="grid-kpi">
      <article class="card">
        <small>Disponibilidad operacional</small>
        <div class="card-value">
          {kpi_disp:.1f}<span class="unit">% </span>
        </div>
        <p class="card-footnote">
          Nivel de disponibilidad del parque de activos en el último mes
          registrado (<strong>{kpi_mes}</strong>).
        </p>
      </article>

      <article class="card">
        <small>Backlog de órdenes de trabajo</small>
        <div class="card-value">
          {kpi_backlog}<span class="unit">OT</span>
        </div>
        <p class="card-footnote">
          Cantidad de órdenes pendientes. Un backlog alto suele anticipar riesgo
          de deterioro operacional si no se gestiona.
        </p>
      </article>

      <article class="card">
        <small>Tickets resueltos dentro de SLA</small>
        <div class="card-value">
          {kpi_sla:.1f}<span class="unit">% </span>
        </div>
        <p class="card-footnote">
          Porcentaje de tickets cerrados dentro del tiempo objetivo.
          Es un proxy directo de calidad y eficiencia del soporte.
        </p>
      </article>
    </section>

    <section class="layout-charts">
      <article class="chart-card">
        <div class="chart-header">
          <h2>Disponibilidad & SLA por mes</h2>
          <span>Serie histórica · %</span>
        </div>
        <canvas id="chartDispSla" height="220"></canvas>
      </article>

      <article class="chart-card">
        <div class="chart-header">
          <h2>Backlog de órdenes de trabajo</h2>
          <span>Trabajo pendiente · unidades</span>
        </div>
        <canvas id="chartBacklog" height="220"></canvas>
      </article>
    </section>

    <footer>
      <span>Portfolio: analytics-tech-portfolio · P09 – Executive HTML Dashboard</span>
      <span>Dataset didáctico · Generado con Python + Pandas + Chart.js</span>
    </footer>
  </div>

  <script>
    const labels = {labels_js};
    const dispData = {disp_js};
    const slaData = {sla_js};
    const backlogData = {backlog_js};

    const ctx1 = document.getElementById('chartDispSla').getContext('2d');
    new Chart(ctx1, {{
      type: 'line',
      data: {{
        labels,
        datasets: [
          {{
            label: 'Disponibilidad operacional (%)',
            data: dispData,
            tension: 0.35,
            borderWidth: 2,
            pointRadius: 3,
          }},
          {{
            label: 'Tickets dentro de SLA (%)',
            data: slaData,
            tension: 0.35,
            borderWidth: 2,
            borderDash: [4, 3],
            pointRadius: 3,
          }}
        ]
      }},
      options: {{
        responsive: true,
        plugins: {{
          legend: {{
            labels: {{
              color: '#e5e7eb',
              font: {{ size: 11 }}
            }}
          }}
        }},
        scales: {{
          x: {{
            ticks: {{ color: '#9ca3af', font: {{ size: 11 }} }},
            grid: {{ color: 'rgba(55,65,81,0.3)' }}
          }},
          y: {{
            ticks: {{ color: '#9ca3af', font: {{ size: 11 }} }},
            grid: {{ color: 'rgba(55,65,81,0.3)' }}
          }}
        }}
      }}
    }});

    const ctx2 = document.getElementById('chartBacklog').getContext('2d');
    new Chart(ctx2, {{
      type: 'bar',
      data: {{
        labels,
        datasets: [
          {{
            label: 'Backlog OT',
            data: backlogData,
            borderWidth: 0,
          }}
        ]
      }},
      options: {{
        responsive: true,
        plugins: {{
          legend: {{
            labels: {{
              color: '#e5e7eb',
              font: {{ size: 11 }}
            }}
          }}
        }},
        scales: {{
          x: {{
            ticks: {{ color: '#9ca3af', font: {{ size: 11 }} }},
            grid: {{ display: false }}
          }},
          y: {{
            ticks: {{ color: '#9ca3af', font: {{ size: 11 }} }},
            grid: {{ color: 'rgba(55,65,81,0.3)' }}
          }}
        }}
      }}
    }});
  </script>
</body>
</html>
"""

# -------------------------------------------------
# 6. Escribir archivo
# -------------------------------------------------
OUTPUT_HTML.write_text(html, encoding="utf-8")
print(f"✅ Dashboard generado en: {OUTPUT_HTML}")
