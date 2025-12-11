
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def main():
    base_dir = Path(__file__).resolve().parent
    project_dir = base_dir / "p09_dashboard_html"
    data_dir = project_dir / "data"
    img_dir = project_dir / "img"

    # Crear estructura de carpetas
    data_dir.mkdir(parents=True, exist_ok=True)
    img_dir.mkdir(parents=True, exist_ok=True)

    # Dataset simple de KPIs mensuales (demo)
    data = {
        "mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
        "disponibilidad_operacional_pct": [92, 90, 88, 93, 95, 94],
        "backlog_ordenes_trabajo": [120, 140, 160, 130, 110, 105],
        "tickets_resueltos_sla_pct": [96, 94, 91, 95, 97, 96],
    }
    df = pd.DataFrame(data)
    csv_path = data_dir / "kpis_operacion_demo.csv"
    df.to_csv(csv_path, index=False)

    # Gráfico 1: Disponibilidad operacional
    plt.figure()
    plt.plot(df["mes"], df["disponibilidad_operacional_pct"], marker="o")
    plt.title("Disponibilidad Operacional")
    plt.xlabel("Mes")
    plt.ylabel("Disponibilidad (%)")
    plt.ylim(80, 100)
    plt.grid(True, linestyle="--", alpha=0.4)
    disp_path = img_dir / "disp_operacional.png"
    plt.tight_layout()
    plt.savefig(disp_path)
    plt.close()

    # Gráfico 2: Backlog de órdenes de trabajo
    plt.figure()
    plt.bar(df["mes"], df["backlog_ordenes_trabajo"])
    plt.title("Backlog de Órdenes de Trabajo")
    plt.xlabel("Mes")
    plt.ylabel("Órdenes pendientes")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    backlog_path = img_dir / "backlog_ot.png"
    plt.tight_layout()
    plt.savefig(backlog_path)
    plt.close()

    # Gráfico 3: Tickets resueltos dentro de SLA
    plt.figure()
    plt.plot(df["mes"], df["tickets_resueltos_sla_pct"], marker="s")
    plt.title("Tickets Resueltos dentro de SLA")
    plt.xlabel("Mes")
    plt.ylabel("Cumplimiento SLA (%)")
    plt.ylim(80, 100)
    plt.grid(True, linestyle="--", alpha=0.4)
    sla_path = img_dir / "tickets_sla.png"
    plt.tight_layout()
    plt.savefig(sla_path)
    plt.close()

    # HTML estático del dashboard
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>P09 – Executive KPI Dashboard</title>
  <style>
    body {{
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      margin: 0;
      padding: 0;
      background: #0b1120;
      color: #e5e7eb;
    }}
    header {{
      padding: 1.5rem 2rem;
      background: linear-gradient(90deg, #1f2937, #0f172a);
      border-bottom: 1px solid #1f2937;
    }}
    h1 {{
      margin: 0;
      font-size: 1.7rem;
    }}
    h2 {{
      margin-top: 0;
    }}
    .tagline {{
      font-size: 0.9rem;
      color: #9ca3af;
    }}
    main {{
      padding: 1.5rem 2rem 2rem;
      max-width: 1100px;
      margin: 0 auto;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.5rem;
      margin-bottom: 2rem;
    }}
    .card {{
      background: #020617;
      border-radius: 1rem;
      border: 1px solid #1f2937;
      padding: 1rem 1.2rem;
      box-shadow: 0 18px 40px rgba(15,23,42,0.7);
    }}
    .kpi-value {{
      font-size: 1.8rem;
      font-weight: 600;
    }}
    .kpi-label {{
      font-size: 0.9rem;
      color: #9ca3af;
      text-transform: uppercase;
      letter-spacing: 0.07em;
    }}
    .kpi-trend-up {{
      color: #4ade80;
      font-size: 0.85rem;
    }}
    .kpi-trend-down {{
      color: #f97373;
      font-size: 0.85rem;
    }}
    .charts {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
    }}
    .chart-card img {{
      width: 100%;
      border-radius: 0.75rem;
      border: 1px solid #1f2937;
      background: #020617;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 0.8rem;
      font-size: 0.9rem;
    }}
    th, td {{
      border: 1px solid #1f2937;
      padding: 0.4rem 0.6rem;
      text-align: center;
    }}
    th {{
      background: #111827;
      font-weight: 500;
    }}
    tbody tr:nth-child(even) {{
      background: #020617;
    }}
    footer {{
      padding: 1rem 2rem 2rem;
      font-size: 0.8rem;
      color: #6b7280;
      text-align: center;
    }}
    a {{
      color: #38bdf8;
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <header>
    <h1>P09 – Executive KPI Dashboard</h1>
    <div class="tagline">Snapshot ejecutivo de desempeño operacional – listo para ser servido como HTML estático.</div>
  </header>
  <main>
    <section>
      <h2>Visión General</h2>
      <p>
        Este dashboard resume la evolución mensual de indicadores clave de operación y soporte
        usando solo HTML estático, imágenes generadas por Python y una tabla de KPIs. Es ideal
        para compartir resultados sin necesidad de servidor, BI corporativo o infraestructura compleja.
      </p>
    </section>

    <section class="grid">
      <article class="card">
        <div class="kpi-label">Disponibilidad Operacional (Jun)</div>
        <div class="kpi-value">{df["disponibilidad_operacional_pct"].iloc[-1]}%</div>
        <div class="kpi-trend-up">Tendencia: estable-alcista vs. trimestre anterior</div>
      </article>
      <article class="card">
        <div class="kpi-label">Backlog Órdenes Trabajo (Jun)</div>
        <div class="kpi-value">{df["backlog_ordenes_trabajo"].iloc[-1]}</div>
        <div class="kpi-trend-up">Reducción gradual desde el peak de Mar</div>
      </article>
      <article class="card">
        <div class="kpi-label">Tickets Resueltos en SLA (Jun)</div>
        <div class="kpi-value">{df["tickets_resueltos_sla_pct"].iloc[-1]}%</div>
        <div class="kpi-trend-up">Estándar >95% sostenido</div>
      </article>
    </section>

    <section>
      <h2>Detalle Mensual de KPIs</h2>
      <table>
        <thead>
          <tr>
            <th>Mes</th>
            <th>Disp. Operacional (%)</th>
            <th>Backlog OT</th>
            <th>Tickets en SLA (%)</th>
          </tr>
        </thead>
        <tbody>
          {''.join(
            f"<tr><td>{row.mes}</td><td>{row.disponibilidad_operacional_pct}</td><td>{row.backlog_ordenes_trabajo}</td><td>{row.tickets_resueltos_sla_pct}</td></tr>"
            for row in df.itertuples()
          )}
        </tbody>
      </table>
    </section>

    <section>
      <h2>Visualizaciones Clave</h2>
      <div class="charts">
        <article class="card chart-card">
          <h3>Disponibilidad Operacional</h3>
          <img src="img/disp_operacional.png" alt="Gráfico de disponibilidad operacional">
        </article>
        <article class="card chart-card">
          <h3>Backlog de Órdenes de Trabajo</h3>
          <img src="img/backlog_ot.png" alt="Gráfico de backlog de órdenes de trabajo">
        </article>
        <article class="card chart-card">
          <h3>Cumplimiento de SLA</h3>
          <img src="img/tickets_sla.png" alt="Gráfico de tickets resueltos dentro de SLA">
        </article>
      </div>
    </section>
  </main>
  <footer>
    Generado con Python + Pandas + Matplotlib → Exportado como HTML estático.<br>
    Ideal para portafolios, PoC ejecutivas y demos sin servidor.
  </footer>
</body>
</html>
"""

    html_path = project_dir / "dashboard.html"
    html_path.write_text(html_content, encoding="utf-8")

    # README simple para P09
    readme_content = """# P09 – Executive KPI Dashboard (Static HTML)

Este proyecto muestra un dashboard ejecutivo construido solo con:
- Python (Pandas + Matplotlib)
- HTML estático + CSS
- Imágenes generadas y referenciadas desde el propio repositorio

## Objetivo

Demostrar cómo exponer KPIs de negocio en un formato ligero, portable y fácil de publicar
(GitHub, carpeta compartida, landing, etc.) sin depender de servidores ni herramientas de BI.

## Cómo reproducir

1. Activar entorno virtual:

   ```bash
   cd "/Users/hugobaghetti/Desktop/PROYECTOS/Proyecto Mineria"
   source .venv/bin/activate
   ```

2. Ejecutar el script de setup (solo una vez):

   ```bash
   python setup_p09_dashboard_html.py
   ```

3. Abrir el dashboard:

   - Desde Finder, abrir:
     `p09_dashboard_html/dashboard.html`
   - O arrastrar el archivo `dashboard.html` a tu navegador favorito.

## Contenido

- `data/kpis_operacion_demo.csv` → Dataset de ejemplo con KPIs mensuales.
- `img/*.png` → Gráficos generados por Matplotlib.
- `dashboard.html` → Dashboard estático navegable.
"""

    readme_path = project_dir / "README.md"
    readme_path.write_text(readme_content, encoding="utf-8")

    print("✅ P09 – Dashboard HTML creado en:", project_dir)
    print("   CSV:", csv_path)
    print("   HTML:", html_path)
    print("   Imágenes:", disp_path.name, backlog_path.name, sla_path.name)

if __name__ == "__main__":
    main()
