# P09 — Executive KPI Dashboard (HTML estático)

_KPIs sin servidor: Python genera gráficos y HTML/CSS los publica._

## Resumen

Soy Hugo Baghetti. En este proyecto construyo un dashboard ejecutivo portable (HTML + CSS) alimentado por gráficos generados en Python. La idea es publicar KPIs sin depender de herramientas de BI ni servidores.

## Por qué hice este proyecto

No siempre hay Power BI / Looker disponible. A veces solo necesitas un artefacto liviano para compartir con una jefatura, o para dejar un tablero en un repositorio. Yo quería demostrar esa alternativa: simple, versionable y publicable en minutos.

## Qué demuestra (en trabajo real)

- Generación de visualizaciones con Python y empaquetado en HTML estático.
- Capacidad de entregar un tablero portable (ideal para GitHub Pages o intranets simples).
- Separación clara: datos → gráficos → presentación.

## Estructura del proyecto

```text
p09_dashboard_html/
├── data/
│   └── kpis_operacion_demo.csv
├── img/
│   └── (gráficos .png generados)
├── dashboard.html
├── setup_p09_dashboard_html.py
└── README.md
```

## Qué hace cada archivo

- `data/kpis_operacion_demo.csv`: dataset de entrada (KPIs por periodo).
- `setup_p09_dashboard_html.py`: genera gráficos y prepara referencias en el HTML.
- `img/`: imágenes generadas por Matplotlib.
- `dashboard.html`: tablero estático consumible por cualquier navegador.

## Instalación

```bash
cd <repository-root>
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
pip install pandas matplotlib
```

## Ejecución

```bash
cd <repository-root>
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
cd p09_dashboard_html

python setup_p09_dashboard_html.py
open dashboard.html
```

## Entradas y salidas

- **Entrada**: `data/kpis_operacion_demo.csv`.
- **Salidas**: gráficos `.png` en `img/` y un `dashboard.html` navegable.

## Metodología (resumen técnico)

- Lectura de KPIs con pandas.
- Generación de visualizaciones con Matplotlib.
- Ensamble de una vista ejecutiva en HTML/CSS referenciando las imágenes del repo.

## Resultados esperables / cómo interpretar

El resultado es un dashboard que se puede:
- adjuntar como carpeta,
- publicar en GitHub Pages,
- compartir por intranet,
- versionar como cualquier código.

## Notas y referencias técnicas

- Dashboards estáticos como alternativa cuando se privilegia portabilidad y cero infraestructura.
- Buenas prácticas: separar datos, generación de figuras y presentación.

## Contacto & Presencia Online

- Email: teleobjetivo.boutique@gmail.com
- Web: www.teleobjetivo.cl
- Instagram: @tele.objetivo
- GitHub: https://github.com/teleobjetivo

**Rol**: University Lecturer (Data & Analytics) · Science Communicator · Research Collaborator

---

## Related Work (Author)

- P01 — Asset Health Analytics for Mining Operations  
- P02 — Maintenance Backlog Prioritization  
- P03 — Failure Pattern Analysis for Conveyor Systems  
- P04 — IT Support Ticket Scoring  
- P05 — Credit Risk Segmentation  
- P06 — Multi-Criteria Scoring for Astrophotography Planning  
- P07 — Scientific Data Pipelines (ALMA-inspired)  
- P08 — Automated Exploratory Data Analysis (DataCopilot)  
- P09 — Static Executive KPI Dashboards  
- P10 — Analytics Readiness Framework  

---

---

## Technical References & Background

1. Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques*. Morgan Kaufmann.
2. Provost, F., & Fawcett, T. (2013). *Data Science for Business*. O’Reilly Media.
3. CRISP-DM 1.0 — Cross-Industry Standard Process for Data Mining.
4. ISO/IEC 25010 — Systems and Software Quality Models.
5. Basel Committee on Banking Supervision. *Principles for the Management of Credit Risk*.

---

---

## Author & Professional Profile

**Hugo Baghetti**  
Applied Analytics Researcher & Scientific Communicator  

**Areas:** Data Analytics · Decision Support Systems · Applied AI · Data Engineering  

**Contact**
- Email: teleobjetivo.boutique@gmail.com  
- Web: https://www.teleobjetivo.cl  
- GitHub: https://github.com/teleobjetivo  
- Instagram (visual science communication): https://www.instagram.com/tele.objetivo  

---
