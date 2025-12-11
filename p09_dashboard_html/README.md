# P09 – Executive KPI Dashboard (Static HTML)

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
